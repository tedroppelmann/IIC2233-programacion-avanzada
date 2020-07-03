
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

WINDOW_NAME, BASE_CLASS = uic.loadUiType("ventana_espera.ui")

class VentanaEspera(WINDOW_NAME, BASE_CLASS):

    signal_sala_espera = None
    signal_usuario_espera = pyqtSignal(dict)
    signal_sala_espera_servidor = None
    signal_error_espera = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()
        self.lista_jugadores = list()

    def init_signals(self):
        self.signal_sala_espera.connect(self.mostrar)
        self.signal_sala_espera_servidor.connect(self.mostrar)
        self.signal_error_espera.connect(self.error)

    def init_gui(self):
        imagen = QPixmap((data['logo_path']))
        self.logo.setPixmap(imagen)

    def error(self):
        self.hide()

    def mostrar(self, data):
        conectados = data['usuarios_conectados']
        valores = data['usuarios_conectados']
        cantidad_jugadores = data['cantidad_jugadores']
        for i in range(0, cantidad_jugadores - len(data['usuarios_conectados'])):
            valores.append('ESPERANDO...')
        if len(self.lista_jugadores) == 0:
            for usuario in valores:
                label = QLabel()
                self.jugadores.addWidget(label)
                label.setText(usuario)
                label.setStyleSheet("color: white")
                self.lista_jugadores.append(label)
        else:
            for jugador, valor in zip(self.lista_jugadores, valores):
                if jugador.text() != valor:
                    jugador.setText(valor)
        self.show()

        if 'ESPERANDO...' not in valores:
            print('Todos los usuarios conectados')
            self.signal_usuario_espera.emit({'evento': 'empezar',
                                             'detalles': '-'})
            self.hide()

        if data['evento'] == 'error servidor':
            self.hide()

if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])

    # Instancio clases
    ventana_espera = VentanaEspera()

    ventana_espera.show()
    sys.exit(app.exec_())