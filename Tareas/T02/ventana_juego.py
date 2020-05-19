
import os
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from drag_and_drop import DraggableLabel, DropLabel
from PyQt5.QtCore import pyqtSignal, Qt

WINDOW_NAME_2, BASE_CLASS_2 = uic.loadUiType("ventana_juego.ui")

class VentanaPrincipal(WINDOW_NAME_2, BASE_CLASS_2):

    #Señales:
    signal_cargar_juego = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_signals(self):
        # Solo una debe activarse
        self.signal_cargar_juego.connect(self.comenzar_juego)

    def init_gui(self):
        self.espacio_posible = QLabel(self.mapa)
        self.espacio_drag_drop = DropLabel(self.mapa)
        # Sacar la parte de la pared y los bordes
        # Son 60 px hasta el borde de arriba pero se le saca 15 px para que se alcance el borde
        # con lo pies.
        self.espacio_posible.setGeometry(0, 45, 430, 240)
        self.espacio_drag_drop.setGeometry(0, 45, 430, 240)
        # Creamos los labels individuales
        self.label_mesero = QLabel(self.espacio_posible)
        self.label_mesas = dict()
        self.label_chefs = dict()
        # No se si va aca esto
        self.drag_and_drop()

    def comenzar_juego(self, datos):
        # Actualizar posiciones personajes
        self.posicion_mesero(datos['mesero'])
        self.posicion_mesas(datos['mesas'])
        self.posicion_chefs(datos['chefs'])
        # Actualizar datos en pantalla
        self.dinero_lcd.display(datos['dinero'])
        self.reputacion_barra.setValue(datos['reputacion'])
        self.ronda.setText(f"RONDA Nº {datos['rondas_terminadas']}")

        self.show()

    def drag_and_drop(self):
        self.dyg_chef = DraggableLabel(self.chef)
        foto = QPixmap(os.path.join('sprites', 'chef', 'meson_01.png'))
        self.dyg_chef.setPixmap(foto)

    # Tengo que hacer que se actualicen y que cambien de foto por movimiento

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
