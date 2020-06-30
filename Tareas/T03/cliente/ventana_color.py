
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal

WINDOW_NAME, BASE_CLASS = uic.loadUiType("ventana_color.ui")

class VentanaColor(WINDOW_NAME, BASE_CLASS):

    signal_elegir_color = None
    signal_color_elegido = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def init_signals(self):
        self.signal_elegir_color.connect(self.init_gui)
        self.boton_amarillo.clicked.connect(self.amarillo)
        self.boton_azul.clicked.connect(self.azul)
        self.boton_rojo.clicked.connect(self.rojo)
        self.boton_verde.clicked.connect(self.verde)

    def init_gui(self):
        self.show()

    def amarillo(self):
        self.signal_color_elegido.emit({'evento': 'color seleccionado',
                                        'detalles': 'amarillo'})
        self.hide()

    def azul(self):
        self.signal_color_elegido.emit({'evento': 'color seleccionado',
                                        'detalles': 'azul'})
        self.hide()

    def rojo(self):
        self.signal_color_elegido.emit({'evento': 'color seleccionado',
                                        'detalles': 'rojo'})
        self.hide()

    def verde(self):
        self.signal_color_elegido.emit({'evento': 'color seleccionado',
                                        'detalles': 'verde'})
        self.hide()
