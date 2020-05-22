
import os
import sys
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from drag_and_drop import DraggableLabel, DropLabel
from PyQt5.QtCore import pyqtSignal, Qt, QRect
import parametros as p

WINDOW_NAME_2, BASE_CLASS_2 = uic.loadUiType("ventana_juego.ui")

class VentanaPrincipal(WINDOW_NAME_2, BASE_CLASS_2):
    #Señales back-end:
    signal_comenzar_juego = None
    signal_drag_and_drop = pyqtSignal(int, int, str)
    signal_comenzar_ronda = pyqtSignal()
    signal_eliminar = pyqtSignal(int, int)
    signal_eliminar_label = None
    signal_crear_drag_and_drop = None
    signal_mover_mesero = pyqtSignal(str)
    signal_update_posicion_mesero = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_signals(self):
        self.signal_comenzar_juego.connect(self.comenzar_juego)
        self.boton_salir.clicked.connect(self.salir)
        self.boton_comenzar_ronda.clicked.connect(self.comenzar_ronda)
        self.signal_eliminar_label.connect(self.eliminar_label)
        self.signal_crear_drag_and_drop.connect(self.agregar_por_drag_drop)
        self.signal_update_posicion_mesero.connect(self.update_posicion_mesero)

    def init_gui(self):
        # La única forma que se me ocurrio para fijar el tamaño del label
        self.mapa.setMaximumSize(p.ANCHO_MAPA, p.LARGO_MAPA)
        self.mapa.setMinimumSize(p.ANCHO_MAPA, p.LARGO_MAPA)
        self.espacio_piso = QLabel(self.mapa)
        self.espacio_drag_drop = DropLabel(self.mapa)
        self.espacio_drag_drop.signal_drag_and_drop = self.signal_drag_and_drop
        self.espacio_piso.setGeometry(0, p.PUNTO_INICIAL_PISO, p.ANCHO_PISO, p.LARGO_PISO)
        # El borde derecho e inferior vienen dados para que quepa el meson del chef sin salirse.
        # Por eso es más pequeño.
        self.espacio_drag_drop.setGeometry(0, p.PUNTO_INICIAL_PISO, p.ANCHO_DRAG_DROP, p.LARGO_DRAG_DROP)
        # Creamos los labels
        self.label_mesero = QLabel(self.espacio_piso)
        self.label_mesas = dict()
        self.label_chefs = dict()
        self.rectangulos = dict()
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
        self.label_mesero.move(mesero.x, mesero.y)

    def posicion_mesas(self, mesas):
        imagen = QPixmap(os.path.join('sprites', 'mapa', 'accesorios', 'mesa_pequena.png'))
        for mesa in mesas:
            print(f'Posicion mesas: {mesa}')
            self.label_mesas[f'({mesas[mesa].x},{mesas[mesa].y})'] = QLabel(self.espacio_piso)
            self.rectangulos[f'mesa,({mesas[mesa].x},{mesas[mesa].y})'] = QRect(mesas[mesa].x, mesas[mesa].y, p.ANCHO_MESA, p.LARGO_MESA)
            self.label_mesas[f'({mesas[mesa].x},{mesas[mesa].y})'].setPixmap(imagen)
            self.label_mesas[f'({mesas[mesa].x},{mesas[mesa].y})'].move(mesas[mesa].x, mesas[mesa].y)
            self.label_mesas[f'({mesas[mesa].x},{mesas[mesa].y})'].show()

    def posicion_chefs(self, chefs):
        imagen = QPixmap(os.path.join('sprites', 'chef', 'meson_01.png'))
        for chef in chefs:
            print(f'Posicion chefs: {chef}')
            self.label_chefs[f'({chefs[chef].x},{chefs[chef].y})'] = QLabel(self.espacio_piso)
            self.rectangulos[f'chef,({chefs[chef].x},{chefs[chef].y})'] = QRect(chefs[chef].x, chefs[chef].y, p.ANCHO_CHEF, p.LARGO_CHEF)
            self.label_chefs[f'({chefs[chef].x},{chefs[chef].y})'].setPixmap(imagen)
            self.label_chefs[f'({chefs[chef].x},{chefs[chef].y})'].move(chefs[chef].x, chefs[chef].y)
            self.label_chefs[f'({chefs[chef].x},{chefs[chef].y})'].show()

    def agregar_por_drag_drop(self, tipo, dinero, x, y):
        if tipo == 'chef':
            imagen = QPixmap(os.path.join('sprites', 'chef', 'meson_01.png'))
            self.label_chefs[f'({x},{y})'] = QLabel(self.espacio_piso)
            self.rectangulos[f'chef,({x},{y})'] = QRect(x, y, p.ANCHO_CHEF, p.LARGO_CHEF)
            self.label_chefs[f'({x},{y})'].setPixmap(imagen)
            self.label_chefs[f'({x},{y})'].move(x, y)
            self.label_chefs[f'({x},{y})'].show()
        elif tipo == 'mesa':
            imagen = QPixmap(os.path.join('sprites', 'mapa', 'accesorios', 'mesa_pequena.png'))
            self.label_mesas[f'({x},{y})'] = QLabel(self.espacio_piso)
            self.rectangulos[f'mesa,({x},{y})'] = QRect(x, y, p.ANCHO_MESA, p.LARGO_MESA)
            self.label_mesas[f'({x},{y})'].setPixmap(imagen)
            self.label_mesas[f'({x},{y})'].move(x, y)
            self.label_mesas[f'({x},{y})'].show()
        self.dinero_lcd.display(dinero)

    def mousePressEvent(self, event):
        # Envío al back-end posiciones válidas dentro del mapa
        pos_x = event.x() - self.mapa.x()
        pos_y = event.y() - self.mapa.y() - p.PUNTO_INICIAL_PISO
        print(pos_x, pos_y)
        if 0 <= pos_x <= p.ANCHO_PISO and 0 <= pos_y <= p.LARGO_PISO:
            self.signal_eliminar.emit(pos_x, pos_y)

    # Elimina la imagen del objeto que se quiere borrar
    def eliminar_label(self, tipo, x, y):
        print("retorna señal")
        print(tipo)
        if tipo == 'chef':
            self.label_chefs[f'({x},{y})'].hide()
            self.label_chefs.pop(f'({x},{y})')
            self.rectangulos.pop(f'chef,({x},{y})')
        elif tipo == 'mesa':
            self.label_mesas[f'({x},{y})'].hide()
            self.label_mesas.pop(f'({x},{y})')
            self.rectangulos.pop(f'mesa,({x},{y})')

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_A:
            self.signal_mover_mesero.emit('A')
        elif event.key() == Qt.Key_D:
            self.signal_mover_mesero.emit('D')
        elif event.key() == Qt.Key_W:
            self.signal_mover_mesero.emit('W')
        elif event.key() == Qt.Key_S:
            self.signal_mover_mesero.emit('S')

    def update_posicion_mesero(self, x, y, frame, posicion):
        self.rectangulo_mesero = QRect(x, y, p.ANCHO_MESERO, p.LARGO_MESERO)
        imagen = QPixmap(os.path.join('sprites', 'mesero', f'{posicion}_0{frame}.png'))
        self.label_mesero.setPixmap(imagen)
        i = 0
        for objeto in self.rectangulos:
            if self.rectangulo_mesero.intersects(self.rectangulos[objeto]):
                self.signal_mover_mesero.emit('ocupado')
                i += 1
        if i == 0:
            self.label_mesero.move(x, y)
            self.show()

    def comenzar_ronda(self):
        self.signal_comenzar_ronda.emit()

    def salir(self):
        sys.exit()