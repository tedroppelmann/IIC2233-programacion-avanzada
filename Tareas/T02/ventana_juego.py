
import os
import sys
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from drag_and_drop import DraggableLabel, DropLabel
from PyQt5.QtCore import pyqtSignal

WINDOW_NAME_2, BASE_CLASS_2 = uic.loadUiType("ventana_juego.ui")

class VentanaPrincipal(WINDOW_NAME_2, BASE_CLASS_2):

    #Señales back-end:
    signal_cargar_juego = None
    signal_drag_and_drop = pyqtSignal(int, int, str)
    signal_comenzar_ronda = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_signals(self):
        self.signal_cargar_juego.connect(self.comenzar_juego)
        # Botones:
        self.boton_salir.clicked.connect(self.salir)
        self.boton_comenzar_ronda.clicked.connect(self.comenzar_ronda)


    def init_gui(self):
        self.espacio_posible = QLabel(self.mapa)
        espacio_drag_drop = DropLabel(self.mapa)
        espacio_drag_drop.signal_drag_and_drop = self.signal_drag_and_drop
        # Sacar la parte de la pared y los bordes
        # Son 60 px hasta el borde de arriba pero se le saca 15 px para que se alcance el borde
        # con lo pies.
        self.espacio_posible.setGeometry(0, 45, 430, 240)
        espacio_drag_drop.setGeometry(0, 45, 430, 240)

        # Creamos los labels individuales
        self.label_mesero = QLabel(self.espacio_posible)
        self.label_mesas = dict()
        self.label_chefs = dict()

        # Hacemos arrastrables los elementos de la tienda
        chef = DraggableLabel(self.chef)
        chef.name = 'chef'
        foto = QPixmap(os.path.join('sprites', 'chef', 'meson_01.png'))
        chef.setPixmap(foto)

        mesa = DraggableLabel(self.mesa)
        mesa.name = 'mesa'
        foto = QPixmap(os.path.join('sprites', 'mapa', 'accesorios', 'mesa_pequena.png'))
        mesa.setPixmap(foto)

    def comenzar_juego(self, datos):
        # Recibo los datos del diccionario que contiene los datos de mapa.csv
        # Actualizar posiciones personajes
        self.posicion_mesero(datos['mesero'])
        self.posicion_mesas(datos['mesas'])
        self.posicion_chefs(datos['chefs'])
        print('Va')
        # Actualizar datos en pantalla
        self.dinero_lcd.display(datos['dinero'])
        self.reputacion_barra.setValue(datos['reputacion'])
        self.ronda.setText(f"RONDA Nº {datos['rondas_terminadas']}")

        self.show()

    # Tengo que hacer que se actualicen y que cambien de foto por movimiento

    def posicion_mesero(self, mesero):
        imagen = QPixmap(os.path.join('sprites', 'mesero', 'down_02.png'))
        self.label_mesero.setPixmap(imagen)
        self.label_mesero.move(mesero.x,mesero.y)

    def posicion_mesas(self, mesas):
        imagen = QPixmap(os.path.join('sprites', 'mapa', 'accesorios', 'mesa_pequena.png'))
        for mesa in mesas:
            self.label_mesas[f'({mesas[mesa].x},{mesas[mesa].y})'] = QLabel(self.espacio_posible)
            self.label_mesas[f'({mesas[mesa].x},{mesas[mesa].y})'].setPixmap(imagen)
            self.label_mesas[f'({mesas[mesa].x},{mesas[mesa].y})'].move(mesas[mesa].x, mesas[mesa].y)
            self.label_mesas[f'({mesas[mesa].x},{mesas[mesa].y})'].show()

    def posicion_chefs(self, chefs):
        imagen = QPixmap(os.path.join('sprites', 'chef', 'meson_01.png'))
        for chef in chefs:
            print(f'Posicion chefs: {chef}')
            self.label_chefs[f'({chefs[chef].x},{chefs[chef].y})'] = QLabel(self.espacio_posible)
            self.label_chefs[f'({chefs[chef].x},{chefs[chef].y})'].setPixmap(imagen)
            self.label_chefs[f'({chefs[chef].x},{chefs[chef].y})'].move(chefs[chef].x, chefs[chef].y)
            self.label_chefs[f'({chefs[chef].x},{chefs[chef].y})'].show()

    def comenzar_ronda(self):
        self.signal_comenzar_ronda.emit()

    def salir(self):
        sys.exit()
