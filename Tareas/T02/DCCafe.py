
import parametros as p
from PyQt5.QtCore import QObject, pyqtSignal
from jugador import Mesero
from entidades import Chef, Mesa

#Back-end

class DCCafe(QObject):
    #Señales front-end:
    signal_cargar_juego = None
    signal_comenzar_juego = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        #Llenar
        self.mesero = None
        self.chefs = dict()
        self.bocadillos = None
        self.clientes = dict()
        self.mesas = dict()

    def init_signals(self):
        self.signal_cargar_juego.connect(self.cargar_mapa)

    def cargar_mapa(self):
        with open(p.RUTA_MAPA, "r", encoding = "utf-8") as archivo:
            filas = archivo.readlines()
            listas = [fila.split(",") for fila in filas]
            for lista in listas:
                if lista[0] == 'mesero':
                    self.mesero = Mesero(int(lista[1]), int(lista[2]))
                elif lista[0] == 'chef':
                    self.chefs[f'({lista[1]},{lista[2]})'] = Chef(int(lista[1]), int(lista[2]))
                elif lista[0] == 'mesa':
                    self.mesas[f'({lista[1]},{lista[2]})'] = Mesa(int(lista[1]), int(lista[2]))
        diccionario = {'mesero': self.mesero, 'chefs': self.chefs, 'mesas': self.mesas}
        self.signal_comenzar_juego.emit(diccionario)




