
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal

WINDOW_NAME_1, BASE_CLASS_1 = uic.loadUiType("ventana_inicio.ui")

class VentanaInicio(WINDOW_NAME_1, BASE_CLASS_1):

    #Señales:
    signal_cargar_juego = pyqtSignal()
    signal_crear_juego = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.boton_juego_cargar.clicked.connect(self.cargar_juego)
        self.boton_juego_crear.clicked.connect(self.crear_juego)

    def cargar_juego(self):
        self.signal_cargar_juego.emit()
        self.hide()

    def crear_juego(self):
        self.signal_crear_juego.emit()
        self.hide()

class VentanaPostRonda:
    pass