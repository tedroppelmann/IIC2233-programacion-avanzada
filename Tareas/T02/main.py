import sys
from PyQt5.QtWidgets import QApplication

from ventanas import VentanaInicio
from ventana_juego import VentanaPrincipal
from DCCafe import DCCafe


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])

    juego = DCCafe()
    ventana_inicio = VentanaInicio()
    ventana_principal = VentanaPrincipal()

    #Conectar señales:
    #cargar juego
    juego.signal_cargar_juego = ventana_inicio.signal_cargar_juego
    ventana_principal.signal_cargar_juego = juego.signal_comenzar_juego
    #crear juego
    ventana_principal.signal_crear_juego = ventana_inicio.signal_crear_juego


    #Iniciar señales
    juego.init_signals()
    ventana_principal.init_signals()


    ventana_inicio.show()
    app.exec()