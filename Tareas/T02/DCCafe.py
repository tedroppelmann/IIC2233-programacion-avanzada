
import parametros as p
from PyQt5.QtCore import QObject, pyqtSignal
from entidades import Mesero, Chef, Mesa
import random

class DCCafe(QObject):
    #Señales con front-end:
    signal_cargar_juego = None
    signal_crear_juego = None
    signal_comenzar_juego = pyqtSignal(dict)
    signal_drag_and_drop = None
    signal_crear_drag_and_drop = pyqtSignal(str, int, int, int)
    signal_comenzar_ronda = None
    signal_eliminar = None
    signal_eliminar_label = pyqtSignal(str, int, int)

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
                # Le saco los arbustos de las esquinas
                if i < 30 and j < 60:
                    self.pixeles_mapa[f'({i},{j})'] = "arbol"
                elif i < 30 and j > p.LARGO_PISO - p.LARGO_ARBOL:
                    self.pixeles_mapa[f'({i},{j})'] = "arbol"
                else:
                    self.pixeles_mapa[f'({i},{j})'] = "libre"

        #Ocupo este diccionario para mandar todas las actualizaciones
        self.diccionario_datos = dict()

    def init_signals(self):
        self.signal_cargar_juego.connect(self.cargar)
        self.signal_crear_juego.connect(self.crear)
        self.signal_drag_and_drop.connect(self.drag_and_drop)
        self.signal_comenzar_ronda.connect(self.comenzar_ronda)
        self.signal_eliminar.connect(self.eliminar)

    def cargar(self):
        print("Se carga juego antiguo")
        self.disponibilidad = False
        with open(p.RUTA_DATOS, "r", encoding="utf-8") as archivo:
            fila_1 = archivo.readline()
            fila_1 = fila_1.strip().split(",")
            self.dinero = int(fila_1[0])
            self.reputacion = int(fila_1[1])
            self.rondas_terminadas += int(fila_1[2])
            fila_2 = archivo.readline()
            fila_2 = fila_2.strip().split(",")

        with open(p.RUTA_MAPA, "r", encoding = "utf-8") as archivo:
            filas = archivo.readlines()
            listas = [fila.strip().split(",") for fila in filas]
            for lista in listas:
                if lista[0] == 'mesero':
                    self.mesero = Mesero(int(lista[1]), int(lista[2]))
                    self.ocupar_pixel(int(lista[1]), int(lista[2]), p.ANCHO_MESERO, p.LARGO_MESERO, 'mesero')
                elif lista[0] == 'chef':
                    self.chefs[f'({lista[1]},{lista[2]})'] = Chef(int(lista[1]), int(lista[2]))
                    self.ocupar_pixel(int(lista[1]), int(lista[2]), p.ANCHO_CHEF, p.LARGO_CHEF, 'chef')
                elif lista[0] == 'mesa':
                    self.mesas[f'({lista[1]},{lista[2]})'] = Mesa(int(lista[1]), int(lista[2]))
                    self.ocupar_pixel(int(lista[1]), int(lista[2]), p.ANCHO_MESA, p.LARGO_MESA, 'mesa')
        i = 0
        for chef in self.chefs:
            self.chefs[chef].platos_terminados = fila_2[i]
            i += 1
        self.update_diccionario_datos()
        self.signal_comenzar_juego.emit(self.diccionario_datos)

    def ocupar_pixel(self, x, y, ancho, largo, tipo):
        for i in range(x, x + ancho + 1):
            for j in range(y, y + largo + 1):
                self.pixeles_mapa[f'({i},{j})'] = [tipo, x, y]

    def crear(self):
        print("Se crea nuevo juego")
        self.agregar_figuras_aleatorias('mesero', p.ANCHO_MESERO, p.LARGO_MESERO, 1)
        self.agregar_figuras_aleatorias('chef', p.ANCHO_CHEF, p.LARGO_CHEF, p.CHEFS_INICIALES)
        self.agregar_figuras_aleatorias('mesa', p.ANCHO_MESA, p.LARGO_MESA, p.MESAS_INICIALES)

        self.update_diccionario_datos()
        self.signal_comenzar_juego.emit(self.diccionario_datos)

    def pixel_ocupado(self, x, y, ancho, largo):
        ocupado = False
        for i in range(x, x + ancho):
            for j in range(y, y + largo):
                if self.pixeles_mapa[f'({i},{j})'] != 'libre':
                    print('Hay uno ocupado')
                    ocupado = True
                    return ocupado
        return ocupado

    def agregar_figuras_aleatorias(self, tipo, ancho, largo, cantidad_inicial):
        for valor in range(cantidad_inicial):
            ocupado = True
            while ocupado:
                x, y = random.randint(0, p.ANCHO_PISO - ancho), random.randint(0, p.LARGO_PISO - largo)
                ocupado = self.pixel_ocupado(x, y, ancho, largo)
                if not ocupado:
                    for i in range(x, x + ancho + 1):
                        for j in range(y, y + largo + 1):
                            self.pixeles_mapa[f'({i},{j})'] = [tipo, x, y]
                    if tipo == 'chef':
                        self.chefs[f'({x},{y})'] = Chef(x, y)
                    elif tipo == 'mesa':
                        self.mesas[f'({x},{y})'] = Mesa(x, y)
                    elif tipo == 'mesero':
                        self.mesero = Mesero(x, y)

    def drag_and_drop(self, pos_x, pos_y, nombre):
        if nombre == 'chef' and self.dinero >= p.PRECIO_CHEF and not self.disponibilidad:
            ocupado = self.pixel_ocupado(pos_x, pos_y, p.ANCHO_CHEF, p.LARGO_CHEF)
            if not ocupado:
                self.dinero -= p.PRECIO_CHEF
                self.chefs[f'({int(pos_x)},{int(pos_y)})'] = Chef(int(pos_x), int(pos_y))
                self.agregar_figuras_drag_drop(pos_x, pos_y, p.ANCHO_CHEF, p.LARGO_CHEF, 'chef')
                self.agregar_mapa_csv('chef', pos_x, pos_y)
                self.update_diccionario_datos()
                # Enviar aprobación a front-end para que visualice.
                # Utilizo la misma señal que al iniciar el juego y cargarlo
                self.signal_crear_drag_and_drop.emit('chef', self.dinero, pos_x, pos_y)
        elif nombre == 'mesa' and self.dinero >= p.PRECIO_MESA and not self.disponibilidad:
            ocupado = self.pixel_ocupado(pos_x, pos_y, p.ANCHO_MESA, p.LARGO_MESA)
            if not ocupado:
                self.dinero -= p.PRECIO_MESA
                self.mesas[f'({int(pos_x)},{int(pos_y)})'] = Mesa(int(pos_x), int(pos_y))
                self.agregar_figuras_drag_drop(pos_x, pos_y, p.ANCHO_MESA, p.LARGO_MESA, 'mesa')
                self.agregar_mapa_csv('mesa', pos_x, pos_y)
                self.update_diccionario_datos()
                self.signal_crear_drag_and_drop.emit('mesa', self.dinero, pos_x, pos_y)

    def agregar_figuras_drag_drop(self, x, y, ancho, largo, tipo):
        for i in range(x, x + ancho + 1):
            for j in range(y, y + largo + 1):
                self.pixeles_mapa[f'({i},{j})'] = [tipo, x, y]

    def eliminar(self, x, y):
        print('llega senal')
        print(self.pixeles_mapa[f'({x},{y})'][0])
        if self.pixeles_mapa[f'({x},{y})'] != 'libre' and not self.disponibilidad :
            print('entra')
            x_origen = self.pixeles_mapa[f'({x},{y})'][1]
            y_origen = self.pixeles_mapa[f'({x},{y})'][2]
            if self.pixeles_mapa[f'({x},{y})'][0] == 'chef' and len(self.chefs) > 1:
                self.liberar_pixeles(x_origen, y_origen, p.ANCHO_CHEF, p.LARGO_CHEF)
                self.chefs.pop(f'({x_origen},{y_origen})')
                self.eliminar_mapa_csv('chef', x_origen, y_origen)
                self.signal_eliminar_label.emit('chef', x_origen, y_origen)
            elif self.pixeles_mapa[f'({x},{y})'][0] == 'mesa' and len(self.mesas) > 1:
                self.liberar_pixeles(x_origen, y_origen, p.ANCHO_MESA, p.LARGO_MESA)
                self.mesas.pop(f'({x_origen},{y_origen})')
                self.eliminar_mapa_csv('mesa', x_origen, y_origen)
                self.signal_eliminar_label.emit('mesa', x_origen, y_origen)
            self.update_diccionario_datos()

    def liberar_pixeles(self, x, y, ancho, largo):
        for i in range(x, x + ancho + 1):
            for j in range(y, y + largo + 1):
                self.pixeles_mapa[f'({i},{j})'] = 'libre'

    def agregar_mapa_csv(self, tipo, x, y):
        with open(p.RUTA_MAPA, "a", encoding="utf-8") as archivo:
            archivo.write(f'{tipo},{x},{y}\n')

    def eliminar_mapa_csv(self, tipo, x, y):
        with open(p.RUTA_MAPA, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
        with open(p.RUTA_MAPA, "w", encoding="utf-8") as archivo:
            for linea in lineas:
                if linea.strip("\n") != f'{tipo},{x},{y}':
                    archivo.write(linea)

    # La ocupo para no escribir esto muchas veces... no se si es bueno
    def update_diccionario_datos(self):
        self.diccionario_datos = {'mesero': self.mesero,
                            'chefs': self.chefs,
                            'mesas': self.mesas,
                            'dinero': self.dinero,
                            'reputacion': self.reputacion,
                            'rondas_terminadas': self.rondas_terminadas}

    def comenzar_ronda(self):
        self.disponibilidad = True