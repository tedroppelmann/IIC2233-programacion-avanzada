
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
import sys

WINDOW_NAME, BASE_CLASS = uic.loadUiType("ventana_final.ui")

class VentanaFinal(WINDOW_NAME, BASE_CLASS):

    signal_volver = pyqtSignal()
    signal_final = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def init_signal(self):
        self.boton_volver.clicked.connect(self.volver)
        self.boton_salir.clicked.connect(self.salir)
        self.signal_final.connect(self.init_gui)

    def init_gui(self, data):
        if data['detalles'] == 'ganador':
            self.mensaje.setText(f'¡GANASTE {data["cliente"]}!')
            self.mensaje.setStyleSheet("color: white")
        else:
            self.mensaje.setText(f'¡PERDISTE {data["cliente"]}!')
            self.mensaje.setStyleSheet("color: white")
        self.show()

    def volver(self):
        self.signal_volver.emit()
        self.hide()

    def salir(self):
        sys.exit()
