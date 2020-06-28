
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
import json
import os
import sys

with open('parametros.json') as file:
    data = json.load(file)

WINDOW_NAME, BASE_CLASS = uic.loadUiType("ventana_juego.ui")

class VentanaJuego(WINDOW_NAME, BASE_CLASS):

    signal_cartas = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.usuario = None
        self.cartas_jugador = dict()
        self.usuarios_conectados = list()
        self.reverso = None

    def init_signals(self):
        self.signal_cartas.connect(self.init_gui)

    def init_gui(self, data):

        if data['evento'] == 'carta jugador':
            imagen = data['imagen']
            carta = QLabel()
            carta.setMaximumSize(78,108)
            pixmap = QPixmap()
            pixmap.loadFromData(imagen, 'png')
            carta.setPixmap(pixmap)
            carta.setScaledContents(True)
            self.cartas_usuario.addWidget(carta)
            self.cartas_jugador[(data['numero'], data['color'])] = carta
            self.show()

        elif data['evento'] == 'carta central':
            imagen = data['imagen']
            carta = QLabel()
            carta.setMaximumSize(78, 108)
            pixmap = QPixmap()
            pixmap.loadFromData(imagen, 'png')
            carta.setPixmap(pixmap)
            carta.setScaledContents(True)
            self.carta_jugada.addWidget(carta)
            self.show()

        elif data['evento'] == 'empezar':
            # guardo el nombre de usuario
            self.usuario = data['cliente']

        elif data['evento'] == 'update cartas contrincantes':
            # agrego los otros jugadores
            self.usuarios_conectados = data['usuarios_conectados']
            print(self.usuario)
            print(self.usuarios_conectados)


            self.show()

        elif data['evento'] == 'carta reverso':
            print('Se guarda el reverso')
            pixmap = QPixmap()
            pixmap.loadFromData(data['detalles'], 'png')
            self.reverso = pixmap
            # la agrego al mazo
            self.mazo.setMaximumSize(78, 108)
            self.mazo.setPixmap(self.reverso)
            self.mazo.setScaledContents(True)


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])

    # Instancio clases
    ventana_juego = VentanaJuego()

    ventana_juego.show()
    sys.exit(app.exec_())