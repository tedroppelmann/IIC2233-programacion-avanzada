
from PyQt5.QtCore import QObject, pyqtSignal
import parametros as p

class Mesero(QObject):

    signal_mover_mesero = pyqtSignal(str)

    signal_update_posicion_mesero = pyqtSignal(dict)

    def __init__(self, x, y):
        super().__init__()
        self.__x = x
        self.__y = y
        self.direccion = 'down'
        self.__frame = 2

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, valor):
        if 0 <= valor <= p.ANCHO_PISO - p.ANCHO_MESERO:
            self.__x = valor

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, valor):
        if 0 <= valor <= p.LARGO_PISO - p.LARGO_MESERO:
            self.__y = valor

    @property
    def frame(self):
        return self.__frame

    @frame.setter
    def frame(self, valor):
        if valor > 3:
            self.__frame = 1
        else:
            self.__frame = valor

    def mover(self, event):
        self.frame += 1
        if event == 'D':
            self.x += p.MOVIMIENTO_PIXELES
            self.direccion = 'right'
            return 'A', self.frame, self.direccion
        if event == 'A':
            self.x -= p.MOVIMIENTO_PIXELES
            self.direccion = 'left'
            return 'D', self.frame, self.direccion
        if event == 'W':
            self.y -= p.MOVIMIENTO_PIXELES
            self.direccion = 'up'
            return 'S', self.frame, self.direccion
        if event == 'S':
            self.y += p.MOVIMIENTO_PIXELES
            self.direccion = 'down'
            return 'W', self.frame, self.direccion

class Chef:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.platos_terminados = 0
        self.estado = 'principiante'

class Mesa:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Cliente:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tipo = None