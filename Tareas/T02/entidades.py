
from PyQt5.QtCore import QObject, pyqtSignal, QThread
import parametros as p
import time
from reloj import Reloj
import random

class Mesero(QObject):

    def __init__(self, x, y):
        super().__init__()
        self.__x = x
        self.__y = y
        self.direccion = 'down'
        self.__frame = 2
        self.ocupado = False

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

class Chef(QThread):

    signal_update_animacion_chef = None

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.platos_terminados = 0
        self.nivel = 1
        self.ocupado = False
        self.__frame = 1
        self.plato_listo = False
        self.activado = False

    @property
    def frame(self):
        return self.__frame

    @frame.setter
    def frame(self, valor):
        if valor > 15:
                self.__frame = 1
        else:
            self.__frame = valor

    def run(self):
        while True:
            if not self.ocupado and self.activado:
                self.ocupado = True
                self.cocinar()
            elif self.plato_listo and self.activado:
                self.entregar_plato()

    def cocinar(self):
        tiempo_cocina = Reloj(1)
        tiempo_cocina.start()
        while tiempo_cocina.value < p.TIEMPO_COCINA:
            time.sleep(0.5)
            self.signal_update_animacion_chef.emit({'x': self.x, 'y': self.y, 'frame': self.frame})
            self.frame += 1
        prob = random.randint(0, 1)
        if prob < 0.3/(self.nivel + 1):
            self.signal_update_animacion_chef.emit({'x': self.x, 'y': self.y, 'frame': 17})
            self.ocupado = False
        else:
            self.plato_listo = True
            self.platos_terminados += 1
            self.signal_update_animacion_chef.emit({'x': self.x, 'y': self.y, 'frame': 16})
        self.activado = False
        tiempo_cocina.finish()

    def entregar_plato(self):
        self.signal_update_animacion_chef.emit({'x': self.x, 'y': self.y, 'frame': 1})
        self.plato_listo = False
        self.activado = False
        self.ocupado = False

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
            if not self.tiempo_espera.pausa:
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
        if not self.tiempo_espera.pausa:
            self.signal_update_animacion_cliente.emit({'x': self.x,
                                                       'y': self.y,
                                                       'tipo': 'se fue',
                                                       'estado': self.estado,
                                                       'atendido': self.atendido,
                                                       'frame': self.frame_desatendido})
            self.tiempo_espera.finish()

