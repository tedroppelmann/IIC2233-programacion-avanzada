
import parametros as p
from PyQt5.QtCore import QObject, pyqtSignal, QThread, QTimer
from entidades import Mesero, Chef, Mesa, Cliente
import random
from collections import defaultdict
import time

class DCCafe(QThread):

    signal_cargar_juego = None
    signal_crear_juego = None
    signal_comenzar_juego = pyqtSignal(dict)
    signal_drag_and_drop = None
    signal_crear_drag_and_drop = pyqtSignal(str, int, int, int)
    signal_comenzar_ronda = None
    signal_eliminar = None
    signal_eliminar_label = pyqtSignal(str, int, int)
    signal_mover_mesero = None
    signal_mover_mesero_2 = None
    signal_update_posicion_mesero = pyqtSignal(int, int, int, str)
    signal_crear_cliente = pyqtSignal(int, int)
    signal_update_animacion_cliente = pyqtSignal(dict)
    signal_cliente_se_fue = None

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
        # Pixeles del mapa que están libres y ocupados
        self.pixeles_mapa = defaultdict(lambda: "Hay puntos del objeto fuera del mapa")
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
        # Truquito para eliminar revertir el cambio de posicion del mesero
        self.tecla_contraria = None
        self.cantidad_atendidos = 0
        self.cantidad_perdidos = 0

    def init_signals(self):
        self.signal_cargar_juego.connect(self.cargar)
        self.signal_crear_juego.connect(self.crear)
        self.signal_drag_and_drop.connect(self.drag_and_drop)
        self.signal_comenzar_ronda.connect(self.comenzar_ronda)
        self.signal_eliminar.connect(self.eliminar)
        self.signal_mover_mesero.connect(self.mover_mesero)
        self.signal_cliente_se_fue.connect(self.eliminar_cliente)

    # Carga en el mapa una partida guardada
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

    # Cambia el estado del pixel para que se vea que ahora está ocupado
    def ocupar_pixel(self, x, y, ancho, largo, tipo):
        for i in range(x, x + ancho + 1):
            for j in range(y, y + largo + 1):
                self.pixeles_mapa[f'({i},{j})'] = [tipo, x, y]

    # Crea una nueva partida con objetos nuevos
    def crear(self):
        print("Se crea nuevo juego")
        self.agregar_figuras_aleatorias('mesero', p.ANCHO_MESERO, p.LARGO_MESERO, 1)
        self.agregar_figuras_aleatorias('chef', p.ANCHO_CHEF, p.LARGO_CHEF, p.CHEFS_INICIALES)
        self.agregar_figuras_aleatorias('mesa', p.ANCHO_MESA, p.LARGO_MESA, p.MESAS_INICIALES)
        self.update_diccionario_datos()
        self.signal_comenzar_juego.emit(self.diccionario_datos)
        self.comenzar_ronda()

    # Retorna si algún pixel que se quiere llenar ya está ocupado
    def pixel_ocupado(self, x, y, ancho, largo):
        ocupado = False
        for i in range(x, x + ancho):
            for j in range(y, y + largo):
                if self.pixeles_mapa[f'({i},{j})'] != 'libre':
                    print('Hay uno ocupado')
                    ocupado = True
                    return ocupado
        return ocupado

    # Agrega figuras aleatorias a los pixeles del mapa al crear un juego nuevo
    def agregar_figuras_aleatorias(self, tipo, ancho, largo, cantidad_inicial):
        for valor in range(cantidad_inicial):
            ocupado = True
            while ocupado:
                x = random.randint(15, p.ANCHO_PISO - ancho)
                y = random.randint(0, p.LARGO_PISO - largo)
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

    # Permite agregar objetos por Drag and Drop
    def drag_and_drop(self, pos_x, pos_y, nombre):
        if nombre == 'chef' and self.dinero >= p.PRECIO_CHEF and not self.disponibilidad:
            ocupado = self.pixel_ocupado(pos_x, pos_y, p.ANCHO_CHEF, p.LARGO_CHEF)
            if not ocupado:
                self.dinero -= p.PRECIO_CHEF
                self.chefs[f'({int(pos_x)},{int(pos_y)})'] = Chef(int(pos_x), int(pos_y))
                self.agregar_figuras_drag_drop(pos_x, pos_y, p.ANCHO_CHEF, p.LARGO_CHEF, 'chef')
                self.agregar_mapa_csv('chef', pos_x, pos_y)
                # Enviar aprobación a front-end para que visualice
                self.signal_crear_drag_and_drop.emit('chef', self.dinero, pos_x, pos_y)
                self.update_datos_csv()
                self.update_diccionario_datos()
        elif nombre == 'mesa' and self.dinero >= p.PRECIO_MESA and not self.disponibilidad:
            ocupado = self.pixel_ocupado(pos_x, pos_y, p.ANCHO_MESA, p.LARGO_MESA)
            if not ocupado:
                self.dinero -= p.PRECIO_MESA
                self.mesas[f'({int(pos_x)},{int(pos_y)})'] = Mesa(int(pos_x), int(pos_y))
                self.agregar_figuras_drag_drop(pos_x, pos_y, p.ANCHO_MESA, p.LARGO_MESA, 'mesa')
                self.agregar_mapa_csv('mesa', pos_x, pos_y)
                self.signal_crear_drag_and_drop.emit('mesa', self.dinero, pos_x, pos_y)
                self.update_datos_csv()
                self.update_diccionario_datos()

    # Agrega objeto por Drag and Drop a los pixeles ocupados
    def agregar_figuras_drag_drop(self, x, y, ancho, largo, tipo):
        for i in range(x, x + ancho + 1):
            for j in range(y, y + largo + 1):
                self.pixeles_mapa[f'({i},{j})'] = [tipo, x, y]

    # Elimina objeto del mapa
    def eliminar(self, x, y):
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
                self.update_datos_csv()
                self.update_diccionario_datos()
            elif self.pixeles_mapa[f'({x},{y})'][0] == 'mesa' and len(self.mesas) > 1:
                self.liberar_pixeles(x_origen, y_origen, p.ANCHO_MESA, p.LARGO_MESA)
                self.mesas.pop(f'({x_origen},{y_origen})')
                self.eliminar_mapa_csv('mesa', x_origen, y_origen)
                self.signal_eliminar_label.emit('mesa', x_origen, y_origen)
                self.update_datos_csv()
                self.update_diccionario_datos()

    # Libera el espacio en pixeles al eliminar un objeto del mapa
    def liberar_pixeles(self, x, y, ancho, largo):
        for i in range(x, x + ancho + 1):
            for j in range(y, y + largo + 1):
                self.pixeles_mapa[f'({i},{j})'] = 'libre'

    # Agregar un nuevo objeto a mapa.csv
    def agregar_mapa_csv(self, tipo, x, y):
        with open(p.RUTA_MAPA, "a", encoding="utf-8") as archivo:
            archivo.write(f'{tipo},{x},{y}\n')

    # Eliminar de mapa.csv algun objeto eliminado
    def eliminar_mapa_csv(self, tipo, x, y):
        with open(p.RUTA_MAPA, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
        with open(p.RUTA_MAPA, "w", encoding="utf-8") as archivo:
            for linea in lineas:
                if linea.strip("\n") != f'{tipo},{x},{y}':
                    archivo.write(linea)

    # Actualiza cualquier cambio en datos.csv
    def update_datos_csv(self):
        linea_1_nueva = f'{self.dinero},{self.reputacion},{self.rondas_terminadas}\n'
        lista_2_nueva = []
        for chef in self.chefs:
            lista_2_nueva.append(str(self.chefs[chef].platos_terminados))
        linea_2_nueva = ','.join(lista_2_nueva)
        with open(p.RUTA_DATOS, "w", encoding="utf-8") as archivo:
            archivo.write(linea_1_nueva)
            archivo.write(linea_2_nueva)

    # Permite actualizar la posicion al mesero y envía la señal al frontend para mover al mesero
    def mover_mesero(self, tecla):
        if self.disponibilidad:
            if tecla != 'ocupado':
                self.liberar_pixeles(self.mesero.x, self.mesero.y, p.ANCHO_MESERO, p.LARGO_MESERO)
                self.tecla_contraria, frame, posicion = self.mesero.mover(tecla)
                self.signal_update_posicion_mesero.emit(self.mesero.x, self.mesero.y, frame, posicion)
            else:
                self.mesero.mover(self.tecla_contraria)

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
        self.start() #Empezamos la ronda

    def run(self):
        cantidad_clientes = self.clientes_ronda()
        print(cantidad_clientes)
        i = 1
        while i <= cantidad_clientes:
            time.sleep(p.LLEGADA_CLIENTES)
            if self.crear_cliente(i):
                i += 1

    def crear_cliente(self, i):
        j = 0
        mesa_disponible = None
        for mesa in self.mesas:
            if self.mesas[mesa].disponibilidad == 'libre':
                self.mesas[mesa].disponibilidad = 'ocupada'
                mesa_disponible = mesa
                j += 1
                break
        if j == 1:
            x = self.mesas[mesa_disponible].x
            y = self.mesas[mesa_disponible].y
            prob = random.randint(0,1)
            if prob <= p.PROB_RELAJADO:
                pos_x = x - p.ANCHO_MESERO
                self.clientes[str(i)] = Cliente(pos_x, y, 'relajado')
            else:
                pos_x = x - p.ANCHO_MESERO
                self.clientes[str(i)] = Cliente(pos_x, y, 'apurado')
            self.signal_crear_cliente.emit(pos_x, y)
            self.clientes[str(i)].signal_update_animacion_cliente = self.signal_update_animacion_cliente
            self.clientes[str(i)].start()
            return True

    def eliminar_cliente(self, cliente):
        x = cliente['x'] + p.ANCHO_MESERO
        y = cliente['y']
        self.mesas[f'({x},{y})'].disponibilidad = 'libre'

    def clientes_ronda(self):
        clientes_ronda = 5 * (1 + self.rondas_terminadas)
        return clientes_ronda