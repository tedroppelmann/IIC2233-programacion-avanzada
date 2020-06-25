
import socket
import threading
from juego import Juego
import json

# Código sacado principalmente de una de las hojas de jupyter de la semana de Networking.

class Servidor:

    def __init__(self, host, port):
        print("Inicializando servidor...")
        self.host = host
        self.port = port
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind_and_listen()
        self.accept_connections()
        self.juego = Juego()

    def bind_and_listen(self):
        self.socket_server.bind((self.host, self.port))
        self.socket_server.listen()
        print(f"Servidor escuchando en {self.host}:{self.port}...")

    def accept_connections(self):
        thread = threading.Thread(target=self.accept_connections_thread)
        thread.start()

    def accept_connections_thread(self):
        print("Servidor aceptando conexiones...")
        while True:
            client_socket, _ = self.socket_server.accept()
            listening_client_thread = threading.Thread(
                target=self.listen_client_thread,
                args=(client_socket,),
                daemon=True)
            listening_client_thread.start()

    @staticmethod
    def send(value, sock):
        msg = json.dumps(value)
        msg_bytes = msg.encode()
        msg_length = len(msg_bytes).to_bytes(4, byteorder='big')
        sock.send(msg_length + msg_bytes)

    def listen_client_thread(self, client_socket):
        print("Servidor conectado a un nuevo cliente...")
        while True:
            try:
                response_bytes_length = client_socket.recv(4)
                response_length = int.from_bytes(
                    response_bytes_length, byteorder='big')
                response = bytearray()

                while len(response) < response_length:
                    read_length = min(4096, response_length - len(response))
                    response.extend(client_socket.recv(read_length))

                received = response.decode()
                decoded = json.loads(received)

                if received is not None:
                    self.analizar_mensaje(decoded, client_socket)

            except json.decoder.JSONDecodeError:
                break

    def analizar_mensaje(self, data, client_socket):
        print("Comando recibido:", data)
        response = dict()
        response['cliente'] = data['cliente']
        response['cantidad_jugadores'] = self.juego.cantidad_jugadores
        if data['evento'] == 'conectarse':
            response['evento'] = 'conectarse'
            if self.juego.usuario_valido(data['cliente'], client_socket):
                response['detalles'] = 'aceptado'
                response['usuarios_conectados'] = self.juego.lista_usuarios
                self.update_sala_espera(response)
            else:
                response['detalles'] = 'rechazado'
                self.send(response, client_socket)
        elif data['evento'] == 'cerrar':
            response['evento'] = 'cerrar'
            del self.juego.usuarios[data['cliente']]
            self.juego.lista_usuarios.remove(data['cliente'])
            response['usuarios_conectados'] = self.juego.lista_usuarios
            self.update_sala_espera(response)

    def update_sala_espera(self, response):
        for usuario in self.juego.lista_usuarios:
            self.send(response, self.juego.usuarios[usuario]['socket'])
