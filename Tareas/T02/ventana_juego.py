
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

    signal_comenzar_juego = None
    signal_drag_and_drop = pyqtSignal(int, int, str)
    signal_comenzar_ronda = pyqtSignal()
    signal_eliminar = pyqtSignal(int, int)
    signal_eliminar_label = None
    signal_crear_drag_and_drop = None
    signal_mover_mesero = pyqtSignal(str)
    signal_update_posicion_mesero = None
    signal_crear_cliente = None
    signal_update_animacion_cliente = None
    signal_cliente_se_fue = pyqtSignal(dict)
    signal_pausar_ronda = pyqtSignal()
    signal_colision_objeto = pyqtSignal(tuple)
    signal_update_animacion_chef = None
    signal_update_display = None

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
        self.signal_crear_cliente.connect(self.crear_cliente)
        self.signal_update_animacion_cliente.connect(self.update_animacion_cliente)
        self.boton_pausar.clicked.connect(self.pausar_ronda)
        self.signal_update_animacion_chef.connect(self.update_animacion_chef)
        self.signal_update_display.connect(self.update_display)

    def init_gui(self):
        # La única forma que se me ocurrio para fijar el tamaño del label
        imagen = QPixmap(os.path.join('sprites', 'mapa', 'mapa_sin_borde_1.png'))
        self.mapa.setMaximumSize(p.ANCHO_MAPA, p.LARGO_MAPA)
        self.mapa.setMinimumSize(p.ANCHO_MAPA, p.LARGO_MAPA)
        self.mapa.setPixmap(imagen)
        self.mapa.setScaledContents(True)
        imagen = QPixmap(os.path.join('sprites', 'otros','logo_negro.png'))
        self.logo.setPixmap(imagen)
        self.logo.setScaledContents(True)
        imagen = QPixmap(os.path.join('sprites', 'otros', 'estrella_amarilla.png'))
        self.reputacion.setPixmap(imagen)
        self.reputacion.setScaledContents(True)
        imagen = QPixmap(os.path.join('sprites', 'otros', 'moneda.png'))
        self.dinero.setPixmap(imagen)
        self.dinero.setScaledContents(True)
        imagen = QPixmap(os.path.join('sprites', 'clientes', 'hamster', 'hamster_01.png'))
        self.hamster.setPixmap(imagen)
        #################################################
        self.espacio_piso = QLabel(self.mapa)
        self.espacio_drag_drop = DropLabel(self.mapa)
        self.espacio_drag_drop.signal_drag_and_drop = self.signal_drag_and_drop
        self.espacio_piso.setGeometry(0, p.PUNTO_INICIAL_PISO, p.ANCHO_PISO, p.LARGO_PISO)
        # El borde derecho e inferior vienen dados para que quepa el meson del chef sin salirse.
        # Por eso es más pequeño.
        self.espacio_drag_drop.setGeometry(0, p.PUNTO_INICIAL_PISO, p.ANCHO_DRAG_DROP, p.LARGO_DRAG_DROP)
        # Creamos los labels
        self.label_mesero = QLabel(self.espacio_piso)
        self.label_char = dict()
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
        self.ronda.setText(f"RONDA Nº {datos['rondas_terminadas'] + 1}")
        self.show()

    def posicion_mesero(self, mesero):
        imagen = QPixmap(os.path.join('sprites', 'mesero', 'down_02.png'))
        self.label_mesero.setPixmap(imagen)
        self.label_mesero.move(mesero.x, mesero.y)

    def posicion_mesas(self, mesas):
        imagen = QPixmap(os.path.join('sprites', 'mapa', 'accesorios', 'mesa_pequena.png'))
        for mesa in mesas:
            x = mesas[mesa].x
            y = mesas[mesa].y
            self.label_char[('mesa', x, y)] = QLabel(self.espacio_piso)
            self.label_char[('mesa', x, y)].setPixmap(imagen)
            self.label_char[('mesa', x, y)].move(x, y)
            self.label_char[('mesa', x, y)].show()

    def posicion_chefs(self, chefs):
        imagen = QPixmap(os.path.join('sprites', 'chef', 'meson_01.png'))
        for chef in chefs:
            x = chefs[chef].x
            y = chefs[chef].y
            self.label_char[('chef', x , y)] = QLabel(self.espacio_piso)
            self.label_char[('chef', x , y)].setPixmap(imagen)
            self.label_char[('chef', x , y)].move(x, y)
            self.label_char[('chef', x , y)].show()

    def agregar_por_drag_drop(self, tipo, dinero, x, y):
        if tipo == 'chef':
            imagen = QPixmap(os.path.join('sprites', 'chef', 'meson_01.png'))
            self.label_char[('chef', x, y)] = QLabel(self.espacio_piso)
            self.label_char[('chef', x, y)].setPixmap(imagen)
            self.label_char[('chef', x, y)].move(x, y)
            self.label_char[('chef', x, y)].show()
        elif tipo == 'mesa':
            imagen = QPixmap(os.path.join('sprites', 'mapa', 'accesorios', 'mesa_pequena.png'))
            self.label_char[('mesa', x, y)] = QLabel(self.espacio_piso)
            self.label_char[('mesa', x, y)].setPixmap(imagen)
            self.label_char[('mesa', x, y)].move(x, y)
            self.label_char[('mesa', x, y)].show()
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
        print(tipo)
        if tipo == 'chef':
            self.label_char[('chef', x, y)].hide()
            self.label_char.pop(('chef', x, y))
        elif tipo == 'mesa':
            self.label_char[('mesa', x, y)].hide()
            self.label_char.pop(('mesa', x, y))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_A:
            self.signal_mover_mesero.emit('A')
        elif event.key() == Qt.Key_D:
            self.signal_mover_mesero.emit('D')
        elif event.key() == Qt.Key_W:
            self.signal_mover_mesero.emit('W')
        elif event.key() == Qt.Key_S:
            self.signal_mover_mesero.emit('S')

    # Actualiza la posicion del mesero en el front-end
    def update_posicion_mesero(self, x, y, frame, posicion, ocupado):
        self.rectangulo_mesero = QRect(x, y, p.ANCHO_MESERO, p.LARGO_MESERO)
        if ocupado:
            imagen = QPixmap(os.path.join('sprites', 'mesero', f'{posicion}_snack_0{frame}.png'))
        elif not ocupado:
            imagen = QPixmap(os.path.join('sprites', 'mesero', f'{posicion}_0{frame}.png'))
        self.label_mesero.setPixmap(imagen)
        self.label_mesero.adjustSize()
        i = 0
        for objeto in self.label_char:
            if self.rectangulo_mesero.intersects(self.label_char[objeto].geometry()):
                self.signal_mover_mesero.emit('ocupado')
                i += 1
                if objeto[0] == 'chef':
                    self.signal_colision_objeto.emit(objeto)
                elif objeto[0] == 'cliente':
                    self.signal_colision_objeto.emit(objeto)
                elif objeto[0] == 'mesa':
                    self.signal_colision_objeto.emit(objeto)
        if i == 0:
            self.label_mesero.move(x, y)

    # Envía la señal para comenzar la ronda
    def comenzar_ronda(self):
        self.signal_comenzar_ronda.emit()

    # Crea los clientes en el mapa
    def crear_cliente(self, pos_x, y):
        x = pos_x -p.ANCHO_CLIENTE
        imagen = QPixmap(os.path.join('sprites', 'clientes', 'hamster', 'hamster_01.png'))
        self.label_char[('cliente', x, y)] = QLabel(self.espacio_piso)
        self.label_char[('cliente', x, y)].setGeometry(0, 0, p.ANCHO_CLIENTE, p.LARGO_CLIENTE)
        self.label_char[('cliente', x, y)].setPixmap(imagen)
        self.label_char[('cliente', x, y)].setScaledContents(True)
        self.label_char[('cliente', x, y)].move(x, y)
        self.label_char[('cliente', x, y)].show()

    # Actualiza el estado del cliente en el mapa y lo hace desaparecer
    def update_animacion_cliente(self, cliente):
        x = cliente['x']
        y = cliente['y']
        tipo = cliente['tipo']
        atendido = cliente['atendido']
        frame = cliente['frame']
        if atendido and tipo != 'se fue':
            imagen = QPixmap(os.path.join('sprites', 'clientes', 'hamster', f'hamster_{frame}.png'))
            self.label_char[('cliente', x, y)].setPixmap(imagen)
            self.label_char[('cliente', x, y)].setScaledContents(True)
        elif not atendido and tipo != 'se fue':
            imagen = QPixmap(os.path.join('sprites', 'clientes', 'hamster', f'hamster_{frame}.png'))
            self.label_char[('cliente', x, y)].setPixmap(imagen)
            self.label_char[('cliente', x, y)].setScaledContents(True)
        elif tipo == 'se fue':
            self.signal_cliente_se_fue.emit(cliente)
            self.label_char[('cliente', x , y)].hide()
            self.label_char.pop(('cliente', x , y))

    def update_animacion_chef(self, chef):
        x = chef['x']
        y = chef['y']
        frame = chef['frame']
        if frame <= 9:
            imagen = QPixmap(os.path.join('sprites', 'chef', f'meson_0{frame}.png'))
        else:
            imagen = QPixmap(os.path.join('sprites', 'chef', f'meson_{frame}.png'))
        self.label_char[('chef', x, y)].setPixmap(imagen)
        self.label_char[('chef', x, y)].setScaledContents(True)

    def update_display(self, datos):
        reputacion = datos['reputacion']
        dinero = datos['dinero']
        ronda = datos['ronda']
        atendidos = datos['atendidos']
        perdidos = datos['perdidos']
        proximos = datos['proximos']
        self.dinero_lcd.display(dinero)
        self.reputacion_barra.setValue(reputacion)
        self.ronda.setText(f"RONDA Nº {ronda + 1}")
        self.atendidos_valor.setText(str(atendidos))
        self.perdidos_valor.setText(str(perdidos))
        self.proximos_valor.setText(str(proximos))

    def pausar_ronda(self):
        self.signal_pausar_ronda.emit()

    def salir(self):
        sys.exit()