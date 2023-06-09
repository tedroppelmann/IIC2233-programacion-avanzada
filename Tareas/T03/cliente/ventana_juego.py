
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, QTimer
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QTransform
import json

with open('parametros.json') as file:
    parametros = json.load(file)

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
        self.indice = 0

        self.timer = QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.borrar_valido)
        self.timer.start()

    def init_signals(self):
        self.signal_cartas.connect(self.init_gui)
        self.boton_gritar.clicked.connect(self.gritar)

    def init_gui(self, data):

        if data['evento'] == 'carta jugador':
            imagen = data['imagen']
            carta = QLabelClick(data['color'], data['numero'])
            carta.setMaximumSize(parametros['ancho_carta'], parametros['largo_carta'])
            pixmap = QPixmap()
            pixmap.loadFromData(imagen, 'png')
            carta.setPixmap(pixmap)
            carta.setScaledContents(True)
            self.cartas_usuario.addWidget(carta)
            self.cartas_jugador.append([data['numero'], data['color'], carta])
            carta.clicked.connect(self.label_click)

        elif data['evento'] == 'carta central':
            imagen = data['imagen']
            self.carta_jugada.setMaximumSize(parametros['ancho_carta'], parametros['largo_carta'])
            pixmap = QPixmap()
            pixmap.loadFromData(imagen, 'png')
            self.carta_jugada.setPixmap(pixmap)
            self.carta_jugada.setScaledContents(True)
            self.color.setText(data['color'])
            self.color.setStyleSheet("color: white")

        elif data['evento'] == 'empezar':
            # guardo el nombre de usuario
            self.usuario = data['cliente']
            self.nombre_jugador_abajo.setText(self.usuario)
            self.nombre_jugador_abajo.setStyleSheet("color: white")

        elif data['evento'] == 'update cartas contrincantes':
            # agrego los otros jugadores
            if len(self.usuarios_conectados) == 0:
                self.usuarios_conectados = data['usuarios_conectados']
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
                t = QTransform()
                t.rotate(-90)
                self.nombre_jugador_derecha.setText(data['cliente'])
                self.nombre_jugador_derecha.setStyleSheet("color: white")
                if data['detalles'] == 0:
                    self.nombre_jugador_derecha.setText('PERDEDOR')
                    self.nombre_jugador_derecha.setStyleSheet("color: white")
                for i in range(0,data['detalles']):
                    carta = QLabel()
                    carta.setMaximumSize(parametros['largo_carta'], parametros['ancho_carta'])
                    carta.setPixmap(self.reverso.transformed(t))
                    carta.setScaledContents(True)
                    self.cartas_jugadores[data['cliente']].append(carta)
                    self.cartas_jugador_derecha.addWidget(carta)
            elif diferencia == -1 or diferencia == 3:
                t = QTransform()
                t.rotate(90)
                self.nombre_jugador_izquierda.setText(data['cliente'])
                self.nombre_jugador_izquierda.setStyleSheet("color: white")
                if data['detalles'] == 0:
                    self.nombre_jugador_izquierda.setText('PERDEDOR')
                    self.nombre_jugador_izquierda.setStyleSheet("color: white")
                for i in range(0, data['detalles']):
                    carta = QLabel()
                    carta.setMaximumSize(parametros['largo_carta'], parametros['ancho_carta'])
                    carta.setPixmap(self.reverso.transformed(t))
                    carta.setScaledContents(True)
                    self.cartas_jugadores[data['cliente']].append(carta)
                    self.cartas_jugador_izquierda.addWidget(carta)
            elif diferencia == 2 or diferencia == -2:
                t = QTransform()
                t.rotate(180)
                self.nombre_jugador_arriba.setText(data['cliente'])
                self.nombre_jugador_arriba.setStyleSheet("color: white")
                if data['detalles'] == 0:
                    self.nombre_jugador_arriba.setText('PERDEDOR')
                    self.nombre_jugador_arriba.setStyleSheet("color: white")
                for i in range(0, data['detalles']):
                    carta = QLabel()
                    carta.setMaximumSize(parametros['ancho_carta'], parametros['largo_carta'])
                    carta.setPixmap(self.reverso.transformed(t))
                    carta.setScaledContents(True)
                    self.cartas_jugadores[data['cliente']].append(carta)
                    self.cartas_jugador_arriba.addWidget(carta)
            self.nuevo = False

        elif data['evento'] == 'carta reverso':
            pixmap = QPixmap()
            pixmap.loadFromData(data['detalles'], 'png')
            self.reverso = pixmap
            # la agrego al mazo
            mazo = QLabelClick('mazo', 'mazo')
            mazo.setMaximumSize(parametros['ancho_carta'], parametros['largo_carta'])
            mazo.setPixmap(self.reverso)
            mazo.setScaledContents(True)
            self.mazo_layout.addWidget(mazo)
            mazo.clicked.connect(self.label_click)

        elif data['evento'] == 'actualizar datos pantalla':
            self.turno.setText(data['turno'])
            self.turno.setStyleSheet("color: white")
            self.accion.setText(data['accion'])
            self.accion.setStyleSheet("color: white")
            if data['color'] is not None:
                self.color.setText(data['color'])
                self.color.setStyleSheet("color: white")

        elif data['evento'] == 'eliminar carta':
            i = 0
            for carta in self.cartas_jugador:
                if carta[0] == data['detalles'][0] and carta[1] == data['detalles'][1] and i == 0:
                    carta[2].hide()
                    self.cartas_jugador.remove(carta)
                    i += 1

        elif data['evento'] == 'perdedor':
            clearLayout(self.cartas_usuario)
            self.nombre_jugador_abajo.setText('¡PERDISTE! Ahora estás en MODO ESPECTADOR')
            self.nombre_jugador_abajo.setStyleSheet("color: white")

        elif data['evento'] == 'jugada invalida':
            self.indice += 1

        if data['evento'] == 'fin del juego':
            self.hide()
            self.usuario = None
            self.cartas_jugador = list()
            self.usuarios_conectados = list()
            self.cartas_jugadores = dict()
            self.reverso = None
            self.nuevo = True

            clearLayout(self.cartas_jugador_derecha)
            clearLayout(self.cartas_jugador_arriba)
            clearLayout(self.cartas_jugador_izquierda)
            clearLayout(self.cartas_usuario)
            clearLayout(self.mazo_layout)
            self.nombre_jugador_derecha.setText('')
            self.nombre_jugador_arriba.setText('')
            self.nombre_jugador_izquierda.setText('')
            self.nombre_jugador_abajo.setText('')

        elif data['evento'] == 'error servidor':
            self.hide()

        else:
            self.show()

    def label_click(self, data):
        if data['color'] == 'mazo':
            self.signal_enviar_mensajes.emit({'cliente': self.usuario,
                                              'evento': 'sacar carta mazo',
                                              'detalles': [data['numero'], data['color']]})
        else:
            self.signal_enviar_mensajes.emit({'cliente': self.usuario,
                                              'evento': 'jugar carta',
                                              'detalles': [data['numero'], data['color']]})

    def gritar(self):
        self.signal_enviar_mensajes.emit({'cliente': self.usuario,
                                          'evento': 'gritar',
                                          'detalles': '-'})

    def borrar_valido(self):
        if self.indice == 1:
            self.jugada_invalida.setText('JUGADA INVÁLIDA')
            self.jugada_invalida.setStyleSheet("color: white")
            self.show()
            self.indice += 1
        elif self.indice == 2:
            self.jugada_invalida.setText('')
            self.show()
            self.indice = 0
        elif self.indice == 3:
            self.timer.stop()

# http://josbalcaen.com/maya-python-pyqt-delete-all-widgets-in-a-layout/

def clearLayout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget() is not None:
            child.widget().deleteLater()
        elif child.layout() is not None:
            clearLayout(child.layout())

# http://www.3engine.net/wp/2015/11/pyqt-como-hacer-que-qlabel-sea-clicable/

class QLabelClick(QLabel):

    clicked = pyqtSignal(dict)

    def __init__(self, color, numero):
        QLabel.__init__(self)
        self.color = color
        self.numero = numero

    def mouseReleaseEvent(self, event):
        self.clicked.emit({'color': self.color, 'numero': self.numero})