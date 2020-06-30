
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
import json
import os
import sys

with open('parametros.json') as file:
    data = json.load(file)

WINDOW_NAME, BASE_CLASS = uic.loadUiType("ventana_inicio.ui")

class VentanaInicio(WINDOW_NAME, BASE_CLASS):

    signal_usuario = pyqtSignal(dict)
    signal_validar_usuario = None
    signal_sala_espera = pyqtSignal(dict)
    signal_volver = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_signals(self):
        self.boton_entrar.clicked.connect(self.ingresar)
        self.signal_validar_usuario.connect(self.validar_usuario)
        self.signal_volver.connect(self.init_gui)

    def init_gui(self):
        imagen = QPixmap((data['logo_path']))
        self.logo.setPixmap(imagen)
        self.nombre_usuario.setText('')
        self.show()

    def ingresar(self):
        user = self.nombre_usuario.text()
        self.signal_usuario.emit({'cliente': user,'evento': 'conectarse','detalles': '-'})

    def validar_usuario(self, data):
        if data['detalles'] == 'rechazado':
            self.nombre_usuario.setText('Nombre inválido')
        else:
            self.signal_sala_espera.emit(data)
            self.hide()


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])

    # Instancio clases
    ventana_inicio = VentanaInicio()

    ventana_inicio.show()
    sys.exit(app.exec_())