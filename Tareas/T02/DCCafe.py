
import parametros as p
from PyQt5.QtCore import QObject, pyqtSignal
from entidades import Mesero, Chef, Mesa, Cliente
import random

class DCCafe(QObject):
    #Señales con front-end:
    signal_cargar_juego = None
    signal_crear_juego = None
    signal_comenzar_juego = pyqtSignal(dict)
    signal_drag_and_drop = None
    signal_comenzar_ronda = None

    def __init__(self):
        super().__init__()
        #Llenar
        self.mesero = None
        self.chefs = dict()
        self.bocadillos = None
        self.clientes = dict()
        self.mesas = dict()
        self.dinero = p.DINERO_INICIAL
        self.reputacion = p.REPUTACION_INICIAL
        self.rondas_terminadas = 0

        self.disponibilidad = True

        self.pixeles_mapa = dict()
        for i in range(0, p.ANCHO_PISO + 1):
            for j in range(0, p.LARGO_PISO + 1):
                self.pixeles_mapa[f'({i},{j})'] = "libre"

        #Ocupo este diccionario para mandar todas las actualizaciones
        self.diccionario_datos = dict()

    def init_signals(self):
        self.signal_cargar_juego.connect(self.cargar)
        self.signal_crear_juego.connect(self.crear)
        self.signal_drag_and_drop.connect(self.drag_and_drop)
        self.signal_comenzar_ronda.connect(self.comenzar_ronda)

    def cargar(self):
        print("Se carga juego antiguo")
        self.disponibilidad = False
        with open(p.RUTA_MAPA, "r", encoding = "utf-8") as archivo:
            filas = archivo.readlines()
            listas = [fila.strip().split(",") for fila in filas]
            for lista in listas:
                if lista[0] == 'mesero':
                    self.mesero = Mesero(int(lista[1]), int(lista[2]))
                elif lista[0] == 'chef':
                    self.chefs[f'({lista[1]},{lista[2]})'] = Chef(int(lista[1]), int(lista[2]))
                elif lista[0] == 'mesa':
                    self.mesas[f'({lista[1]},{lista[2]})'] = Mesa(int(lista[1]), int(lista[2]))

        with open(p.RUTA_DATOS, "r", encoding="utf-8") as archivo:
            fila_1 = archivo.readline()
            fila_1 = fila_1.strip().split(",")
            self.dinero = int(fila_1[0])
            self.reputacion = int(fila_1[1])
            self.rondas_terminadas += int(fila_1[2])
            fila_2 = archivo.readline()
            fila_2 = fila_2.strip().split(",")
            # falta agregar los platos terminados por chef

        self.update_diccionario_datos()
        self.signal_comenzar_juego.emit(self.diccionario)

    def crear(self):
        print("Se crea nuevo juego")
        self.agregar_figuras('mesero', p.ANCHO_MESERO, p.LARGO_MESERO, 1)
        self.agregar_figuras('chef', p.ANCHO_CHEF, p.LARGO_CHEF, p.CHEFS_INICIALES)
        self.agregar_figuras('mesa', p.ANCHO_MESA, p.LARGO_MESA, p.MESAS_INICIALES)

        self.update_diccionario_datos()
        self.signal_comenzar_juego.emit(self.diccionario)

    def pixel_ocupado(self, ancho, largo):

        ocupado = False
        x, y = random.randint(0, p.ANCHO_PISO - ancho), random.randint(0, p.LARGO_PISO - largo)
        for i in range(x, x + ancho):
            for j in range(y, y + largo):
                if self.pixeles_mapa[f'({i},{j})'] == 'ocupado':
                    print('Hay uno ocupado')
                    ocupado = True
                    return ocupado, x, y
        return ocupado, x, y

    def agregar_figuras(self, tipo, ancho, largo, cantidad_inicial):

        for valor in range(cantidad_inicial):
            ocupado = True
            while ocupado:
                ocupado, x, y = self.pixel_ocupado(ancho, largo)
                if not ocupado:
                    for i in range(x, x + ancho + 1):
                        for j in range(y, y + largo + 1):
                            self.pixeles_mapa[f'({i},{j})'] = 'ocupado'
                    if tipo == 'chef':
                        self.chefs[f'({x},{y})'] = Chef(x, y)
                    elif tipo == 'mesa':
                        self.mesas[f'({x},{y})'] = Mesa(x, y)
                    elif tipo == 'mesero':
                        self.mesero = Mesero(x, y)

    def drag_and_drop(self, pos_x, pos_y, nombre):

        if nombre == 'chef' and self.dinero >= p.PRECIO_CHEF and not self.disponibilidad:
            self.dinero -= p.PRECIO_CHEF
            self.chefs[f'({int(pos_x)},{int(pos_y)})'] = Chef(int(pos_x), int(pos_y))
            self.update_mapa_csv('chef', pos_x, pos_y)
            self.update_diccionario_datos()
            # Enviar aprobación a front-end para que visualice.
            # Utilizo la misma señal que al iniciar el juego y cargarlo
            self.signal_comenzar_juego.emit(self.diccionario)

        elif nombre == 'mesa' and self.dinero >= p.PRECIO_MESA and not self.disponibilidad:
            self.dinero -= p.PRECIO_MESA
            self.mesas[f'({int(pos_x)},{int(pos_y)})'] = Mesa(int(pos_x), int(pos_y))
            self.update_mapa_csv('mesa', pos_x, pos_y)
            self.update_diccionario_datos()
            self.signal_comenzar_juego.emit(self.diccionario)

    def update_mapa_csv(self, tipo, x, y):

        with open(p.RUTA_MAPA, "a", encoding="utf-8") as archivo:
            archivo.write(f'{tipo},{x},{y}\n')

    # La ocupo para no escribir esto muchas veces... no se si es bueno
    def update_diccionario_datos(self):

        self.diccionario = {'mesero': self.mesero,
                            'chefs': self.chefs,
                            'mesas': self.mesas,
                            'dinero': self.dinero,
                            'reputacion': self.reputacion,
                            'rondas_terminadas': self.rondas_terminadas}

    def comenzar_ronda(self):
        self.disponibilidad = True