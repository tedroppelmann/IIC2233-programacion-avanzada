
import os
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel

WINDOW_NAME_2, BASE_CLASS_2 = uic.loadUiType("ventana_juego.ui")

class VentanaJuego(WINDOW_NAME_2, BASE_CLASS_2):

    #Señales:
    signal_cargar_juego = None
    signal_crear_juego = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_signals(self):
        self.signal_cargar_juego.connect(self.comenzar_juego)

    def init_gui(self):
        self.espacio_posible = QLabel(self.mapa)
        #Sacar la parte de la pared y los bordes
        self.espacio_posible.setGeometry(10, 50, 400, 250)
        self.label_mesero = QLabel(self.espacio_posible)
        self.label_mesas = dict()
        self.label_chefs = dict()

    def comenzar_juego(self, datos):
        self.posicion_mesero(datos['mesero'])
        self.posicion_mesas(datos['mesas'])
        self.posicion_chefs(datos['chefs'])
        self.show()

    def posicion_mesero(self, mesero):
        imagen = QPixmap(os.path.join('sprites', 'mesero', 'down_02.png'))
        self.label_mesero.setPixmap(imagen)
        self.label_mesero.move(mesero.x,mesero.y)

    def posicion_mesas(self, mesas):
        imagen = QPixmap(os.path.join('sprites', 'mapa', 'accesorios', 'silla_mesa_amarilla.png'))
        for mesa in mesas:
            self.label_mesas['mesa'] = QLabel(self.espacio_posible)
            self.label_mesas['mesa'].setPixmap(imagen)
            self.label_mesas['mesa'].move(mesas[mesa].x, mesas[mesa].y)

    def posicion_chefs(self, chefs):
        imagen = QPixmap(os.path.join('sprites', 'chef', 'meson_01.png'))
        for chef in chefs:
            print(chef)
            self.label_chefs['chef'] = QLabel(self.espacio_posible)
            self.label_chefs['chef'].setPixmap(imagen)
            self.label_chefs['chef'].move(chefs[chef].x, chefs[chef].y)


