
import socket
import threading
from juego import Juego
import json
import base64
import time
from generador_de_mazos import sacar_cartas

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
        self.empezar = 0

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
        numero_validacion = 0
        msg_tipo = numero_validacion.to_bytes(4, byteorder='big')
        sock.send(msg_tipo + msg_length + msg_bytes)

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

            except ConnectionResetError:
                print("Error de conexión con el cliente!")

    def analizar_mensaje(self, data, client_socket):
        print("Comando recibido:", data)
        response = dict()
        response['cliente'] = data['cliente']
        response['cantidad_jugadores'] = self.juego.cantidad_jugadores
        if data['evento'] == 'conectarse':
            response['evento'] = 'conectarse'
            if self.juego.usuario_valido(data['cliente'], client_socket):
                print(f'Cliente {data["cliente"]} ingresó a la sala de espera')
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

        elif data['evento'] == 'empezar':
            self.empezar += 1
            self.juego.poblar_cartas(data['cliente'])
            for carta in self.juego.usuarios[data['cliente']]['cartas']:
                self.enviar_carta(carta, client_socket)
            time.sleep(1)
            self.update_cartas_contrincantes(data['cliente'])
            if self.empezar == self.juego.cantidad_jugadores:
                if self.juego.carta_jugada is None:
                    print('Juego listo para empezar')
                    carta = sacar_cartas(1)
                    self.juego.carta_jugada = carta
                    print(self.juego.carta_jugada)
                    '''
                    for usuario in self.juego.usuarios:
                        self.enviar_carta(self.juego.carta_jugada, self.juego.usuarios[usuario]['socket'])'''



    def update_sala_espera(self, response):
        for usuario in self.juego.lista_usuarios:
            self.send(response, self.juego.usuarios[usuario]['socket'])
            self.enviar_carta(('reverso','reverso'), self.juego.usuarios[usuario]['socket'])

    def enviar_carta(self, carta, sock):
        numero = carta[0]
        color = carta[1]
        if carta[0] == 'color':
            with open(f"sprites/simple/color.png", "rb") as file:
                bytes_imagen = base64.b64encode(file.read())
        elif carta[0] == 'reverso':
            with open(f"sprites/simple/reverso.png", "rb") as file:
                bytes_imagen = base64.b64encode(file.read())
        else:
            with open(f"sprites/simple/{numero}_{color}.png", "rb") as file:
                bytes_imagen = base64.encodebytes(file.read())
        id_color = 1
        id_numero = 2
        id_imagen = 3
        bytes_id_color = id_color.to_bytes(4, byteorder='big')
        bytes_id_numero = id_numero.to_bytes(4, byteorder='big')
        bytes_id_imagen = id_imagen.to_bytes(4, byteorder='big')
        bytes_largo_color = len(color.encode()).to_bytes(4, byteorder='little')
        bytes_largo_numero = len(numero.encode()).to_bytes(4, byteorder='little')
        bytes_largo_imagen = len(bytes_imagen).to_bytes(4, byteorder='little')
        bytes_color = color.encode()
        bytes_numero = numero.encode()
        bcolor = bytes_id_color + bytes_largo_color + bytes_color
        bnumero = bytes_id_numero + bytes_largo_numero + bytes_numero
        bimagen = bytes_id_imagen + bytes_largo_imagen + bytes_imagen
        mensaje = bytearray(bcolor + bnumero + bimagen)
        sock.send(mensaje)

    def update_cartas_contrincantes(self, user):
        mensaje = dict()
        mensaje['evento'] = 'update cartas contrincantes'
        mensaje['usuarios_conectados'] = self.juego.lista_usuarios
        for usuario in self.juego.lista_usuarios:
            cartas = self.juego.cantidad_cartas(usuario)
            mensaje['cliente'] = usuario
            mensaje['detalles'] = cartas
            if usuario != user:
                self.send(mensaje, self.juego.usuarios[user]['socket'])





if __name__ == '__main__':
    servidor = Servidor("localhost", 8080)
    servidor.enviar_carta(('4', 'rojo'))
    numero = 0
    msg_tipo = numero.to_bytes(4, byteorder='little')

    print(msg_tipo)