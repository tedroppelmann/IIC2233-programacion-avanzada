
from PyQt5.QtCore import QObject, pyqtSignal, QThread
import parametros as p
import time
from reloj import Reloj

class Mesero(QObject):

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
            self.x += p.VEL_MOVIMIENTO
            self.direccion = 'right'
            return 'A', self.frame, self.direccion
        if event == 'A':
            self.x -= p.VEL_MOVIMIENTO
            self.direccion = 'left'
            return 'D', self.frame, self.direccion
        if event == 'W':
            self.y -= p.VEL_MOVIMIENTO
            self.direccion = 'up'
            return 'S', self.frame, self.direccion
        if event == 'S':
            self.y += p.VEL_MOVIMIENTO
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
        self.disponibilidad = 'libre'

class Cliente(QThread):

    signal_update_animacion_cliente = None

    def __init__(self, x, y, tipo):
        super().__init__()
        self.x = x
        self.y = y
        self.tipo = tipo #RELAJADO O APURADO o se va
        self.tiempo_espera = Reloj(0.5)
        self.estado = 'alegre'
        self.atendido = False
        self.__frame_desatendido = 26
        self.__frame_enojado = 18
        self.diccionario_datos = dict()

    @property
    def frame_desatendido(self):
        return self.__frame_desatendido

    @frame_desatendido.setter
    def frame_desatendido(self, valor):
        if valor > 30:
            self.__frame_desatendido = 26
        else:
            self.__frame_desatendido = valor

    @property
    def frame_enojado(self):
        return self.__frame_enojado

    @frame_enojado.setter
    def frame_enojado(self, valor):
        if valor > 24:
            self.__frame_enojado = 18
        else:
            self.__frame_enojado = valor

    def run(self):
        if not self.atendido:
            if self.tipo == 'relajado':
                self.espera_cliente(p.TIEMPO_ESPERA_RELAJADO)
            elif self.tipo == 'apurado':
                self.espera_cliente(p.TIEMPO_ESPERA_APURADO)

    def espera_cliente(self, tipo):
        self.tiempo_espera.start()
        while self.tiempo_espera.value < tipo:
            if self.tiempo_espera.value >= tipo / 2:
                if self.tiempo_espera.value >= tipo - 1.5:
                    time.sleep(0.5)
                    self.signal_update_animacion_cliente.emit({'x': self.x,
                                                               'y': self.y,
                                                               'tipo': self.tipo,
                                                               'estado': self.estado,
                                                               'atendido': self.atendido,
                                                               'frame': self.frame_enojado})
                    self.frame_enojado += 3
                else:
                    time.sleep(0.5)
                    self.signal_update_animacion_cliente.emit({'x': self.x,
                                                               'y': self.y,
                                                               'tipo': self.tipo,
                                                               'estado': self.estado,
                                                               'atendido': self.atendido,
                                                               'frame': self.frame_desatendido})
                    self.frame_desatendido += 1
        self.signal_update_animacion_cliente.emit({'x': self.x,
                                                   'y': self.y,
                                                   'tipo': 'se fue',
                                                   'estado': self.estado,
                                                   'atendido': self.atendido,
                                                   'frame': self.frame_desatendido})
        self.tiempo_espera.finish()

