
import sys
import json
from PyQt5.QtWidgets import QApplication
from ventana_inicio import VentanaInicio
from cliente import Cliente
from ventana_espera import VentanaEspera
from ventana_juego import VentanaJuego


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])

    # Instancio clases
    ventana_inicio = VentanaInicio()
    ventana_espera = VentanaEspera()
    ventana_juego = VentanaJuego()
    cliente = Cliente()

    # Conexión señales
    # nombre usuario:
    cliente.signal_usuario = ventana_inicio.signal_usuario
    ventana_inicio.signal_validar_usuario = cliente.signal_validar_usuario
    # sala espera:
    ventana_espera.signal_sala_espera = ventana_inicio.signal_sala_espera
    cliente.signal_usuario_espera = ventana_espera.signal_usuario_espera
    ventana_espera.signal_sala_espera_servidor = cliente.signal_sala_espera_servidor
    # cartas:
    ventana_juego.signal_cartas = cliente.signal_cartas

    # Iniciar señales
    ventana_inicio.init_signals()
    ventana_espera.init_signals()
    ventana_juego.init_signals()
    cliente.init_signals()

    ventana_inicio.show()
    sys.exit(app.exec_())

