import os
import sys
from random import choice

from PyQt5.QtWidgets import QLabel, QWidget, QLineEdit, \
    QHBoxLayout, QVBoxLayout, QPushButton, QGridLayout
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication


class VentanaPrincipal(QWidget):

    # Aquí debes crear una señal que usaras para enviar la jugada al back-end
    senal_enviar_jugada = pyqtSignal(dict)

    def __init__(self, *args):
        super().__init__(*args)
        self.crear_pantalla()
        self.datos = None


    def crear_pantalla(self):
        # Aquí deben crear la ventana vacia.
        self.setWindowTitle("DCCuent")
        # Es decir, agregar y crear labels respectivos a datos del juego, pero sin contenido
        # Si usas layout recuerda agregar los labels al layout y finalmente setear el layout
        self.label_1 = QLabel()
        self.label_2 = QLabel()
        self.label_3 = QLabel()

        self.label_4 = QLabel("Q", self)
        self.label_5 = QLabel("W", self)
        self.label_6 = QLabel("E", self)

        self.label_7 = QLabel()
        self.label_7.setGeometry(1, 1, 238, 452)
        self.label_8 = QLabel()
        self.label_8.setGeometry(1, 1, 238, 452)
        self.label_9 = QLabel()
        self.label_9.setGeometry(1, 1, 238, 452)

        self.grilla = QGridLayout()
        self.grilla.addWidget(self.label_1, 0, 0)
        self.grilla.addWidget(self.label_2, 0, 1)
        self.grilla.addWidget(self.label_3, 0, 2)
        self.grilla.addWidget(self.label_4, 1, 0)
        self.grilla.addWidget(self.label_5, 1, 1)
        self.grilla.addWidget(self.label_6, 1, 2)
        self.grilla.addWidget(self.label_7, 2, 0)
        self.grilla.addWidget(self.label_8, 2, 1)
        self.grilla.addWidget(self.label_9, 2, 2)
        self.setLayout(self.grilla)


    def actualizar(self, datos):
        self.datos = datos
        # Esta es la funcion que se encarga de actualizar el contenido de la ventana y abrirla
        # Recibe las nuevas cartas y la puntuación actual en un diccionario
        self.label_1.setText(f"Usuario: {datos['usuario']}")
        self.label_2.setText(f"Victorias: {datos['victorias']}")
        self.label_3.setText(f"Derrotas: {datos['derrotas']}")
        pixeles_1 = QPixmap(datos['infanteria']['ruta']).scaled(238, 452)
        self.label_7.setPixmap(pixeles_1)
        pixeles_2 = QPixmap(datos['rango']['ruta']).scaled(238, 452)
        self.label_8.setPixmap(pixeles_2)
        pixeles_3 = QPixmap(datos['artilleria']['ruta']).scaled(238, 452)
        self.label_9.setPixmap(pixeles_3)
        # Al final, se muestra la ventana.
        self.show()

    def keyPressEvent(self, evento):
        # Aquí debes capturar la techa apretara,
        # y enviar la carta que es elegida
        if evento.text() == "q":
            self.senal_enviar_jugada.emit(self.datos['infanteria'])
            self.hide()
        elif evento.text() == "w":
            self.senal_enviar_jugada.emit(self.datos['rango'])
            self.hide()
        elif evento.text() == "e":
            self.senal_enviar_jugada.emit(self.datos['artilleria'])
            self.hide()



class VentanaCombate(QWidget):

    # Esta señal es para volver a la VentanaPrincipal con los datos actualizados
    senal_regresar = pyqtSignal(dict)
    # Esta señal envia a la ventana final con el resultado del juego
    senal_abrir_ventana_final = pyqtSignal(str)

    def __init__(self, *args):
        super().__init__(*args)
        self.crear_pantalla()

    def crear_pantalla(self):
        self.setWindowTitle("DCCuent")
        self.vbox = QVBoxLayout()
        self.layout_principal = QHBoxLayout()
        self.label_carta_usuario = QLabel()
        self.label_victoria = QLabel()
        self.label_carta_enemiga = QLabel()
        self.boton_regresar = QPushButton("Regresar")

        self.layout_principal.addWidget(self.label_carta_usuario)
        self.layout_principal.addWidget(self.label_victoria)
        self.layout_principal.addWidget(self.label_carta_enemiga)

        self.boton_regresar.clicked.connect(self.regresar)
        self.vbox.addLayout(self.layout_principal)
        self.vbox.addWidget(self.boton_regresar)

        self.setLayout(self.vbox)

    def mostrar_resultado_ronda(self, datos):
        self.datos = datos
        mensaje = datos["mensaje"]
        carta_enemiga = datos["enemigo"]
        carta_jugador = datos["jugador"]
        self.label_carta_usuario.setPixmap(QPixmap(carta_jugador["ruta"]).scaled(238,452))
        self.label_carta_enemiga.setPixmap(QPixmap(carta_enemiga["ruta"]).scaled(238,452))
        self.label_victoria.setText(mensaje)
        self.show()

    def regresar(self):
        resultado = self.datos["resultado"]
        if resultado == "victoria" or resultado == "derrota":
            self.senal_abrir_ventana_final.emit(resultado)
        else:
            self.senal_regresar.emit(self.datos)
        self.hide()


if __name__ == "__main__":
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    a = QApplication(sys.argv)
    ventana_principal = VentanaPrincipal()

    ventana_principal.show()
    sys.exit(a.exec())
