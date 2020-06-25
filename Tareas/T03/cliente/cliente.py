
import socket
import threading
import json
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal

with open('parametros.json') as file:
    data = json.load(file)
host = data['host']
port = data['port']

# Código sacado principalmente de una de las hojas de jupyter de la semana de Networking. 

class Cliente(QObject):

    signal_usuario = None
    signal_validar_usuario = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        print("Inicializando cliente...")
        self.host = host
        self.port = port
        self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.connect_to_server()
            self.listen()

        except ConnectionError:
            print("Conexión terminada.")
            self.socket_client.close()
            exit()

    def init_signals(self):
        self.signal_usuario.connect(self.send)

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
            response_bytes_length = self.socket_client.recv(4)
            response_length = int.from_bytes(
                response_bytes_length, byteorder='big')
            response = bytearray()
            # Recibimos datos hasta que alcancemos la totalidad de los datos
            # indicados en los primeros 4 bytes recibidos.
            while len(response) < response_length:
                read_length = min(4096, response_length - len(response))
                response.extend(self.socket_client.recv(read_length))

            received = response.decode()
            decoded = json.loads(received)

            print(f"{decoded}\n>>> ", end='')

            self.analizar_mensaje(decoded)

    def analizar_mensaje(self, data):

        if data['evento'] == 'conectarse':
            self.signal_validar_usuario.emit(data)


