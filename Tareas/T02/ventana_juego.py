
import os
import sys
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from drag_and_drop import DraggableLabel, DropLabel
from PyQt5.QtCore import pyqtSignal
import parametros as p

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
        # La única forma que se me ocurrio para fijar el tamaño del label
        self.mapa.setMaximumSize(p.ANCHO_MAPA, p.LARGO_MAPA)
        self.mapa.setMinimumSize(p.ANCHO_MAPA, p.LARGO_MAPA)
        self.espacio_piso = QLabel(self.mapa)
        espacio_drag_drop = DropLabel(self.mapa)
        espacio_drag_drop.signal_drag_and_drop = self.signal_drag_and_drop
        self.espacio_piso.setGeometry(0, p.PUNTO_INICIAL_PISO, p.ANCHO_PISO, p.LARGO_PISO)
        # El borde derecho e inferior vienen dados para que quepa el meson del chef sin salirse.
        # Por eso es más pequeño.
        espacio_drag_drop.setGeometry(0, p.PUNTO_INICIAL_PISO, p.ANCHO_DRAG_DROP, p.LARGO_DRAG_DROP)

        # Creamos los labels individuales
        self.label_mesero = QLabel(self.espacio_piso)
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
            print(f'Posicion mesas: {mesa}')
            self.label_mesas[f'({mesas[mesa].x},{mesas[mesa].y})'] = QLabel(self.espacio_piso)
            self.label_mesas[f'({mesas[mesa].x},{mesas[mesa].y})'].setPixmap(imagen)
            self.label_mesas[f'({mesas[mesa].x},{mesas[mesa].y})'].move(mesas[mesa].x, mesas[mesa].y)
            self.label_mesas[f'({mesas[mesa].x},{mesas[mesa].y})'].show()

    def posicion_chefs(self, chefs):
        imagen = QPixmap(os.path.join('sprites', 'chef', 'meson_01.png'))
        for chef in chefs:
            print(f'Posicion chefs: {chef}')
            self.label_chefs[f'({chefs[chef].x},{chefs[chef].y})'] = QLabel(self.espacio_piso)
            self.label_chefs[f'({chefs[chef].x},{chefs[chef].y})'].setPixmap(imagen)
            self.label_chefs[f'({chefs[chef].x},{chefs[chef].y})'].move(chefs[chef].x, chefs[chef].y)
            self.label_chefs[f'({chefs[chef].x},{chefs[chef].y})'].show()

    def comenzar_ronda(self):
        self.signal_comenzar_ronda.emit()

    def salir(self):
        sys.exit()