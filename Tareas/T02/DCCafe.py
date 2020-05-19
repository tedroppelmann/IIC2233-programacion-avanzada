
import parametros as p
from PyQt5.QtCore import QObject, pyqtSignal
from entidades import Mesero, Chef, Mesa, Cliente

class DCCafe(QObject):
    #Señales front-end:
    signal_cargar_juego = None
    signal_crear_juego = None
    signal_comenzar_juego = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        #Llenar
        self.mesero = None
        self.chefs = dict()
        self.bocadillos = None
        self.clientes = dict()
        self.mesas = dict()
        self.dinero = 0
        self.reputacion = 0
        self.rondas_terminadas = 0

    def init_signals(self):
        self.signal_cargar_juego.connect(self.cargar)
        self.signal_crear_juego.connect(self.crear)

    def cargar(self):
        print("Se carga juego antiguo")
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
            self.dinero += int(fila_1[0])
            self.reputacion += int(fila_1[1])
            self.rondas_terminadas += int(fila_1[2])
            fila_2 = archivo.readline()
            fila_2 = fila_2.strip().split(",")
            # falta agregar los platos terminados por chef

        diccionario = {'mesero': self.mesero,
                       'chefs': self.chefs,
                       'mesas': self.mesas,
                       'dinero': self.dinero,
                       'reputacion': self.reputacion,
                       'rondas_terminadas': self.rondas_terminadas}

        self.signal_comenzar_juego.emit(diccionario)

    def crear(self):
        print("Se crea nuevo juego")
        self.mesero = Mesero(p.POS_INICIAL_MESERO_X,p.POS_INICIAL_MESERO_Y)

        diccionario = {'mesero': self.mesero,
                       'chefs': self.chefs,
                       'mesas': self.mesas,
                       'dinero': self.dinero,
                       'reputacion': self.reputacion,
                       'rondas_terminadas': self.rondas_terminadas}

        self.signal_comenzar_juego.emit(diccionario)










