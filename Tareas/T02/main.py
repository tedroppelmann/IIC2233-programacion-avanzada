import sys
from PyQt5.QtWidgets import QApplication

from ventanas import VentanaInicio
from ventana_juego import VentanaPrincipal
from DCCafe import DCCafe
from drag_and_drop import DropLabel


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])

    juego = DCCafe()
    ventana_inicio = VentanaInicio()
    ventana_principal = VentanaPrincipal()

    # Conectar señales:
    # cargar juego
    juego.signal_cargar_juego = ventana_inicio.signal_cargar_juego
    ventana_principal.signal_cargar_juego = juego.signal_comenzar_juego
    # crear juego
    juego.signal_crear_juego = ventana_inicio.signal_crear_juego
    # drag and drop
    juego.signal_drag_and_drop = ventana_principal.signal_drag_and_drop
    # comenzar ronda
    juego.signal_comenzar_ronda = ventana_principal.signal_comenzar_ronda



    # Iniciar señales:
    juego.init_signals()
    ventana_principal.init_signals()


    ventana_inicio.show()
    app.exec()