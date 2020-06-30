
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QTransform
import json
import os
import sys

with open('parametros.json') as file:
    data = json.load(file)

WINDOW_NAME, BASE_CLASS = uic.loadUiType("ventana_juego.ui")

class VentanaJuego(WINDOW_NAME, BASE_CLASS):

    signal_cartas = None
    signal_enviar_mensajes = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.usuario = None
        self.cartas_jugador = list()
        self.usuarios_conectados = list()
        self.cartas_jugadores = dict()
        self.reverso = None
        self.nuevo = True

    def init_signals(self):
        self.signal_cartas.connect(self.init_gui)

    def init_gui(self, data):

        if data['evento'] == 'carta jugador':
            imagen = data['imagen']
            carta = QLabelClick(data['color'], data['numero'])
            carta.setMaximumSize(78,108)
            pixmap = QPixmap()
            pixmap.loadFromData(imagen, 'png')
            carta.setPixmap(pixmap)
            carta.setScaledContents(True)
            self.cartas_usuario.addWidget(carta)
            self.cartas_jugador.append([data['numero'], data['color'], carta])
            carta.clicked.connect(self.label_click)
            self.show()

        elif data['evento'] == 'carta central':
            imagen = data['imagen']
            self.carta_jugada.setMaximumSize(78, 108)
            pixmap = QPixmap()
            pixmap.loadFromData(imagen, 'png')
            self.carta_jugada.setPixmap(pixmap)
            self.carta_jugada.setScaledContents(True)
            self.color.setText(data['color'])
            self.color.setStyleSheet("color: white")
            self.show()

        elif data['evento'] == 'empezar':
            # guardo el nombre de usuario
            self.usuario = data['cliente']

        elif data['evento'] == 'update cartas contrincantes':
            # agrego los otros jugadores
            self.usuarios_conectados = data['usuarios_conectados']
            print(self.usuarios_conectados)
            self.nombre_jugador_abajo.setText(self.usuario)
            self.nombre_jugador_abajo.setStyleSheet("color: white")
            indice_user = self.usuarios_conectados.index(self.usuario)
            indice_otro = self.usuarios_conectados.index(data['cliente'])
            diferencia = indice_otro - indice_user
            if self.nuevo:
                for usuario in data['usuarios_conectados']:
                    self.cartas_jugadores[usuario] = list()
            else:
                for carta in self.cartas_jugadores[data['cliente']]:
                    carta.hide()
            if diferencia == 1 or diferencia == -3:
                print('Se pone en la derecha')
                t = QTransform()
                t.rotate(-90)
                self.nombre_jugador_derecha.setText(data['cliente'])
                self.nombre_jugador_derecha.setStyleSheet("color: white")
                for i in range(0,data['detalles']):
                    carta = QLabel()
                    carta.setMaximumSize(108, 78)
                    carta.setPixmap(self.reverso.transformed(t))
                    carta.setScaledContents(True)
                    self.cartas_jugadores[data['cliente']].append(carta)
                    self.cartas_jugador_derecha.addWidget(carta)
            elif diferencia == -1 or diferencia == 3:
                print('Se pone en la izquierda')
                t = QTransform()
                t.rotate(90)
                self.nombre_jugador_izquierda.setText(data['cliente'])
                self.nombre_jugador_izquierda.setStyleSheet("color: white")
                for i in range(0, data['detalles']):
                    carta = QLabel()
                    carta.setMaximumSize(108, 78)
                    carta.setPixmap(self.reverso.transformed(t))
                    carta.setScaledContents(True)
                    self.cartas_jugadores[data['cliente']].append(carta)
                    self.cartas_jugador_izquierda.addWidget(carta)
            elif diferencia == 2 or diferencia == -2:
                print('Se pone arriba')
                t = QTransform()
                t.rotate(180)
                self.nombre_jugador_arriba.setText(data['cliente'])
                self.nombre_jugador_arriba.setStyleSheet("color: white")
                for i in range(0, data['detalles']):
                    carta = QLabel()
                    carta.setMaximumSize(78, 108)
                    carta.setPixmap(self.reverso.transformed(t))
                    carta.setScaledContents(True)
                    self.cartas_jugadores[data['cliente']].append(carta)
                    self.cartas_jugador_arriba.addWidget(carta)
            self.nuevo = False
            self.show()

        elif data['evento'] == 'carta reverso':
            print('Se guarda el reverso')
            pixmap = QPixmap()
            pixmap.loadFromData(data['detalles'], 'png')
            self.reverso = pixmap
            # la agrego al mazo
            mazo = QLabelClick('mazo', 'mazo')
            mazo.setMaximumSize(78, 108)
            mazo.setPixmap(self.reverso)
            mazo.setScaledContents(True)
            self.mazo_layout.addWidget(mazo)
            mazo.clicked.connect(self.label_click)

        elif data['evento'] == 'actualizar datos pantalla':
            print('LLEGA CAMBIO DE PANTALLA')
            self.turno.setText(data['turno'])
            self.turno.setStyleSheet("color: white")
            self.accion.setText(data['accion'])
            self.accion.setStyleSheet("color: white")
            self.show()

        elif data['evento'] == 'eliminar carta':
            i = 0
            for carta in self.cartas_jugador:
                if carta[0] == data['detalles'][0] and carta[1] == data['detalles'][1] and i == 0:
                    carta[2].hide()
                    self.cartas_jugador.remove(carta)
                    i += 1

    def label_click(self, data):
        print('CLICK')
        print(data['color'])
        print(data['numero'])
        if data['color'] == 'mazo':
            self.signal_enviar_mensajes.emit({'cliente': self.usuario,
                                              'evento': 'sacar carta mazo',
                                              'detalles': [data['numero'], data['color']]})
        else:
            self.signal_enviar_mensajes.emit({'cliente': self.usuario,
                                              'evento': 'jugar carta',
                                              'detalles': [data['numero'], data['color']]})


# http://www.3engine.net/wp/2015/11/pyqt-como-hacer-que-qlabel-sea-clicable/

class QLabelClick(QLabel):

    clicked = pyqtSignal(dict)

    def __init__(self, color, numero):
        QLabel.__init__(self)
        self.color = color
        self.numero = numero

    def mouseReleaseEvent(self, event):
        self.clicked.emit({'color': self.color, 'numero': self.numero})

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