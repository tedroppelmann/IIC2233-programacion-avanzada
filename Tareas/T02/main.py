import sys
from PyQt5.QtWidgets import QApplication

from ventanas import VentanaInicio, VentanaPostRonda
from ventana_juego import VentanaPrincipal
from DCCafe import DCCafe


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])

    #Instancio clases
    juego = DCCafe()
    ventana_inicio = VentanaInicio()
    ventana_principal = VentanaPrincipal()
    ventana_post_ronda = VentanaPostRonda()

    # Conectar señales:
    # cargar juego
    juego.signal_cargar_juego = ventana_inicio.signal_cargar_juego
    ventana_principal.signal_comenzar_juego = juego.signal_comenzar_juego
    # crear juego
    juego.signal_crear_juego = ventana_inicio.signal_crear_juego
    # drag and drop
    juego.signal_drag_and_drop = ventana_principal.signal_drag_and_drop
    ventana_principal.signal_crear_drag_and_drop = juego.signal_crear_drag_and_drop
    # eliminar compra
    juego.signal_eliminar = ventana_principal.signal_eliminar
    ventana_principal.signal_eliminar_label = juego.signal_eliminar_label
    # comenzar ronda
    juego.signal_comenzar_ronda = ventana_principal.signal_comenzar_ronda
    # mover mesero
    juego.signal_mover_mesero = ventana_principal.signal_mover_mesero
    ventana_principal.signal_update_posicion_mesero = juego.signal_update_posicion_mesero



    # Iniciar señales:
    juego.init_signals()
    ventana_principal.init_signals()



    ventana_inicio.show()
    app.exec()