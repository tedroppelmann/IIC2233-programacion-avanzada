
import socket
import threading
import json
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal
import base64

with open('parametros.json') as file:
    data = json.load(file)
host = data['host']
port = data['port']

# Código sacado principalmente de una de las hojas de jupyter de la semana de Networking
# (para el envío de mensajes entre cliente y servidor).

class Cliente(QObject):

    signal_usuario = None
    signal_validar_usuario = pyqtSignal(dict)
    signal_usuario_espera = None
    signal_sala_espera_servidor = pyqtSignal(dict)
    signal_cartas = pyqtSignal(dict)
    signal_enviar_mensaje = None
    signal_elegir_color = pyqtSignal()
    signal_color_elegido = None
    signal_final = pyqtSignal(dict)
    signal_error = pyqtSignal()
    signal_error_espera = pyqtSignal(dict)
    signal_error_inicio = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        print("Inicializando cliente...")
        self.host = host
        self.port = port
        self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.usuario = None
            self.otros_jugadores = None
            self.cartas_usuario = list()
            self.recibir_carta = True
            self.reverso = None
            self.connect_to_server()
            self.listen()

        except ConnectionError:
            self.terminar_conexion()

    def init_signals(self):
        self.signal_usuario.connect(self.enviar_mensaje_servidor)
        self.signal_usuario_espera.connect(self.enviar_mensaje_servidor)
        self.signal_enviar_mensaje.connect(self.enviar_mensaje_servidor)
        self.signal_color_elegido.connect(self.enviar_mensaje_servidor)

    def connect_to_server(self):
        self.socket_client.connect((self.host, self.port))
        print("Cliente conectado exitosamente al servidor.")

    def listen(self):
        thread = threading.Thread(target=self.listen_thread, daemon=True)
        thread.start()

    def send(self, data):
        msg = json.dumps(data)
        msg_bytes = msg.encode()
        msg_length = len(msg_bytes).to_bytes(4, byteorder='big')
        self.socket_client.sendall(msg_length + msg_bytes)

    def listen_thread(self):
        while True:
            try:
                id_color_bytes = self.socket_client.recv(4)
                id_color = int.from_bytes(id_color_bytes, byteorder='big')
                if id_color == 0:
                    response_bytes_length = self.socket_client.recv(4)
                    response_length = int.from_bytes(
                        response_bytes_length, byteorder='big')
                    response = bytearray()
                    while len(response) < response_length:
                        read_length = min(4096, response_length - len(response))
                        response.extend(self.socket_client.recv(read_length))

                    received = response.decode()
                    decoded = json.loads(received)

                    self.recibir_mensaje_servidor(decoded)

                else:
                    largo_color_bytes = self.socket_client.recv(4)
                    largo_color = int.from_bytes(largo_color_bytes, byteorder='little')
                    color = bytearray()
                    while len(color) < largo_color:
                        read_length = min(4096, largo_color - len(color))
                        color.extend(self.socket_client.recv(read_length))

                    id_numero_bytes = self.socket_client.recv(4)
                    id_numero = int.from_bytes(id_numero_bytes, byteorder='big')
                    largo_numero_bytes = self.socket_client.recv(4)
                    largo_numero = int.from_bytes(largo_numero_bytes, byteorder='little')
                    numero = bytearray()
                    while len(numero) < largo_numero:
                        read_length = min(4096, largo_numero - len(numero))
                        numero.extend(self.socket_client.recv(read_length))

                    id_imagen_bytes = self.socket_client.recv(4)
                    id_imagen = int.from_bytes(id_imagen_bytes, byteorder='big')
                    largo_imagen_bytes = self.socket_client.recv(4)
                    largo_imagen = int.from_bytes(largo_imagen_bytes, byteorder='little')
                    imagen = bytearray()
                    while len(imagen) < largo_imagen:
                        read_length = min(4096, largo_imagen - len(imagen))
                        imagen.extend(self.socket_client.recv(read_length))

                    color_decode = color.decode()
                    numero_decode = numero.decode()
                    imagen_decode = base64.decodebytes(imagen)

                    if numero_decode == 'reverso':
                        self.reverso = imagen_decode
                        self.signal_cartas.emit({'evento': 'carta reverso',
                                                 'detalles': self.reverso})

                    else:
                        if self.recibir_carta:
                            carta = {'evento':'carta jugador',
                                     'color':color_decode,
                                     'numero': numero_decode,
                                     'imagen': imagen_decode}
                            self.signal_cartas.emit(carta)
                        else:
                            carta = {'evento': 'carta central',
                                     'color': color_decode,
                                     'numero': numero_decode,
                                     'imagen': imagen_decode}
                            self.signal_cartas.emit(carta)

            except json.decoder.JSONDecodeError or ConnectionResetError:
                self.signal_cartas.emit({'evento': 'error servidor'})
                self.signal_error_espera.emit({'evento': 'error servidor'})
                self.signal_error_inicio.emit({'evento': 'error servidor'})
                self.signal_error.emit()
                break

    def recibir_mensaje_servidor(self, data):
        print(data)
        if data['evento'] == 'conectarse':
            if self.usuario is None and data['detalles'] == 'aceptado':
                self.usuario = data['cliente']
            self.signal_validar_usuario.emit(data)
        elif data['evento'] == 'cerrar':
            self.signal_sala_espera_servidor.emit(data)
        elif data['evento'] == 'update cartas contrincantes':
            self.signal_cartas.emit(data)
        elif data['evento'] == 'actualizar carta central':
            self.recibir_carta = False
        elif data['evento'] == 'actualizar carta central_2':
            self.recibir_carta = True
        elif data['evento'] == 'actualizar datos pantalla':
            self.signal_cartas.emit(data)
        elif data['evento'] == 'eliminar carta':
            self.signal_cartas.emit(data)
        elif data['evento'] == 'activar carta color':
            self.signal_elegir_color.emit()
        elif data['evento'] == 'perdedor':
            self.signal_cartas.emit(data)
        elif data['evento'] == 'fin del juego':
            self.signal_cartas.emit(data)
            self.signal_final.emit(data)
            self.enviar_mensaje_servidor({'cliente': data['cliente'],
                                          'evento': 'reiniciar',
                                          'detalles': '-'})
            self.reiniciar()
        elif data['evento'] == 'jugada invalida':
            self.signal_cartas.emit(data)

    def enviar_mensaje_servidor(self, data):
        if data['evento'] == 'conectarse':
            self.send(data)
        elif data['evento'] == 'empezar':
            data['cliente'] = self.usuario
            self.signal_cartas.emit(data)
            self.send(data)
        elif data['evento'] == 'jugar carta':
            self.send(data)
        elif data['evento'] == 'sacar carta mazo':
            self.recibir_carta = True
            self.send(data)
        elif data['evento'] == 'color seleccionado':
            data['cliente'] = self.usuario
            self.send(data)
        elif data['evento'] == 'reiniciar':
            self.send(data)
        elif data['evento'] == 'gritar':
            self.send(data)

    def reiniciar(self):
        self.usuario = None
        self.otros_jugadores = None
        self.cartas_usuario = list()
        self.recibir_carta = True
        self.reverso = None

    def terminar_conexion(self):
        print('Conexión terminada')
        self.socket_client.close()
        exit()
