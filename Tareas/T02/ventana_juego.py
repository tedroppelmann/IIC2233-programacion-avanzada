
import os
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel

WINDOW_NAME_2, BASE_CLASS_2 = uic.loadUiType("ventana_juego.ui")

class VentanaPrincipal(WINDOW_NAME_2, BASE_CLASS_2):

    #Señales:
    signal_cargar_juego = None
    signal_crear_juego = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_signals(self):
        self.signal_cargar_juego.connect(self.comenzar_juego_cargado)
        self.signal_crear_juego.connect(self.comenzar_juego_nuevo)

    def init_gui(self):
        self.espacio_posible = QLabel(self.mapa)
        # Sacar la parte de la pared y los bordes
        # Son 60 px hasta el borde de arriba pero se le saca 15 px para que se alcance el borde
        # con lo pies.
        self.espacio_posible.setGeometry(0, 45, 430, 240)
        self.label_mesero = QLabel(self.espacio_posible)
        self.label_mesas = dict()
        self.label_chefs = dict()

    def comenzar_juego_cargado(self, datos):
        self.posicion_mesero(datos['mesero'])
        self.posicion_mesas(datos['mesas'])
        self.posicion_chefs(datos['chefs'])
        self.dinero_lcd.display(datos['dinero'])
        self.reputacion_barra.setValue(datos['reputacion'])
        self.ronda.setText(f"RONDA Nº {datos['rondas_terminadas'] + 1}")
        self.show()

    def comenzar_juego_nuevo(self):
        self.show()

    #tengo que hacer que se actualicen y que cambien de foto por movimiento

    def posicion_mesero(self, mesero):
        imagen = QPixmap(os.path.join('sprites', 'mesero', 'down_02.png'))
        self.label_mesero.setPixmap(imagen)
        self.label_mesero.move(mesero.x,mesero.y)

    def posicion_mesas(self, mesas):
        imagen = QPixmap(os.path.join('sprites', 'mapa', 'accesorios', 'mesa_pequena.png'))
        for mesa in mesas:
            self.label_mesas['mesa'] = QLabel(self.espacio_posible)
            self.label_mesas['mesa'].setPixmap(imagen)
            self.label_mesas['mesa'].move(mesas[mesa].x, mesas[mesa].y)

    def posicion_chefs(self, chefs):
        imagen = QPixmap(os.path.join('sprites', 'chef', 'meson_01.png'))
        for chef in chefs:
            self.label_chefs['chef'] = QLabel(self.espacio_posible)
            self.label_chefs['chef'].setPixmap(imagen)
            self.label_chefs['chef'].move(chefs[chef].x, chefs[chef].y)


