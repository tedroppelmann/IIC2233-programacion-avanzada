import sys

from PyQt5.QtWidgets import QLabel, QWidget, QLineEdit, \
    QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication

from parametros import ruta_logo


class VentanaInicial(QWidget):

    # Esta señal es para enviar un intento de nombre de usuario
    senal_revisar_nombre = pyqtSignal(str)

    def __init__(self, *args):
        super().__init__(*args)
        self.crear_pantalla()


    def crear_pantalla(self):
        # Aqui deben crear la pantalla.
        self.setWindowTitle("Ventana Inicial DCCuent")
        # El logo, la caja de texto y el botón.
        # IMPORTANTE la caja de texto debe llamarse input_usuario
        # Si usas layout recuerda agregar los labels al layout y finalmente setear el layout
        self.label1 = QLabel(self)
        self.label1.setGeometry(5, 5, 400, 400)
        pixeles = QPixmap(ruta_logo)
        self.label1.setPixmap(pixeles)
        self.label1.setScaledContents(True)

        self.label2 = QLabel('Ingrese su nombre de usuario:', self)
        self.input_usuario = QLineEdit('', self)
        self.boton1 = QPushButton('&Ingresar', self)
        self.boton1.clicked.connect(self.revisar_input)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.label2)
        hbox.addWidget(self.input_usuario)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addLayout(hbox)
        vbox.addWidget(self.boton1)
        self.setLayout(vbox)


    def revisar_input(self):
        # Aquí deben enviar el nombre de usuario, para verificar si es un usuario valido
        # Para esto utilizar senal_revisar_nombre
        self.senal_revisar_nombre.emit(self.input_usuario.text())


    def recibir_revision(self, error):
        # Resetea la ventana si es que ocurre algun error,en caso contrario comienza el juego
        # IMPORTANTE la caja de text debe llamarse input_usuario
        if error:
            self.input_usuario.clear()
            self.input_usuario.setPlaceholderText("¡Inválido! Debe ser alfa-numérico.")
        else:
            usuario = self.input_usuario.text()
            self.hide()


if __name__ == "__main__":
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    a = QApplication(sys.argv)
    ventana_inicial = VentanaInicial()

    ventana_inicial.show()
    sys.exit(a.exec())
