
import socket
import threading
import json
import base64
import time
from generador_de_mazos import sacar_cartas
from itertools import cycle

with open('parametros.json') as file:
    data = json.load(file)

# Código sacado principalmente de una de las hojas de jupyter de la semana de Networking.

class Servidor:

    def __init__(self, host, port):
        print("Inicializando servidor...")
        self.host = host
        self.port = port
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind_and_listen()
        self.accept_connections()

        self.empezar = 0

        self.usuarios = dict()
        self.lista_usuarios = list()
        self.ciclo = None
        self.cantidad_jugadores = data['cantidad_jugadores']
        self.carta_jugada = None
        self.turno = None
        self.accion = None

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
                response_length = int.from_bytes(response_bytes_length, byteorder='big')
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
        response['cantidad_jugadores'] = self.cantidad_jugadores
        if data['evento'] == 'conectarse':
            response['evento'] = 'conectarse'
            if self.usuario_valido(data['cliente'], client_socket):
                print(f'Cliente {data["cliente"]} ingresó a la sala de espera')
                response['detalles'] = 'aceptado'
                response['usuarios_conectados'] = self.lista_usuarios
                self.update_sala_espera(response)
            else:
                response['detalles'] = 'rechazado'
                self.send(response, client_socket)

        elif data['evento'] == 'cerrar':
            response['evento'] = 'cerrar'
            del self.usuarios[data['cliente']]
            self.lista_usuarios.remove(data['cliente'])
            response['usuarios_conectados'] = self.lista_usuarios
            self.update_sala_espera(response)

        elif data['evento'] == 'empezar':
            self.empezar += 1
            self.poblar_cartas(data['cliente'])
            for carta in self.usuarios[data['cliente']]['cartas']:
                self.enviar_carta(carta, client_socket)
            time.sleep(0.5)
            self.update_cartas_contrincantes(data['cliente'])
            if self.empezar == self.cantidad_jugadores:
                if self.carta_jugada is None:
                    print('Juego listo para empezar')
                    self.ciclo = cycle(self.lista_usuarios)
                    for usuario in self.usuarios:
                        self.enviar_carta(('reverso', 'reverso'), self.usuarios[usuario]['socket'])
                    self.turno = next(self.ciclo)
                    carta = sacar_cartas(1)[0]
                    self.carta_jugada = carta
                    # envío la primera carta a todos los usuarios
                    self.actualizar_carta_central()
                    self.update_datos_pantalla()

        elif data['evento'] == 'jugar carta' or data['evento'] == 'sacar carta mazo':
            self.jugar_turno(data)

    def actualizar_carta_central(self):
        for usuario in self.usuarios:
            self.send({'evento': 'actualizar carta central'},
                      self.usuarios[usuario]['socket'])
            self.enviar_carta(self.carta_jugada,
                              self.usuarios[usuario]['socket'])

    def update_sala_espera(self, response):
        for usuario in self.lista_usuarios:
            self.send(response, self.usuarios[usuario]['socket'])

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
        mensaje['usuarios_conectados'] = self.lista_usuarios
        for usuario in self.lista_usuarios:
            cartas = self.cantidad_cartas(usuario)
            mensaje['cliente'] = usuario
            mensaje['detalles'] = cartas
            if usuario != user:
                self.send(mensaje, self.usuarios[user]['socket'])

    def update_datos_pantalla(self):
        mensaje = dict()
        mensaje['evento'] = 'actualizar datos pantalla'
        for usuario in self.lista_usuarios:
            mensaje['cliente'] = usuario
            mensaje['turno'] = self.turno
            mensaje['accion'] = self.accion
            self.send(mensaje, self.usuarios[usuario]['socket'])

    def usuario_valido(self, user, socket):
        if user.isalnum() and user not in self.usuarios and len(self.lista_usuarios) < self.cantidad_jugadores:
            self.usuarios[user] = {'nombre_usuario': user, 'socket': socket, 'cartas': []}
            self.lista_usuarios.append(user)
            return True
        else:
            return False

    def poblar_cartas(self, usuario):
        self.usuarios[usuario]['cartas'] = sacar_cartas(data['cartas_iniciales'])
        print(self.usuarios[usuario]['nombre_usuario'],self.usuarios[usuario]['cartas'])
        # agregamos la primera carta en juego

    def cantidad_cartas(self, usuario):
        return len(self.usuarios[usuario]['cartas'])

    def jugar_turno(self, data):
        if self.turno == data['cliente'] and self.accion is None:
            numero = data['detalles'][0]
            color = data['detalles'][1]
            if self.carta_jugada[0] == numero or self.carta_jugada[1] == color:
                self.carta_jugada = (numero, color)
                self.usuarios[data['cliente']]['cartas'].remove(self.carta_jugada)
                self.send({'cliente': data['cliente'],
                           'evento': 'eliminar carta',
                           'detalles': self.carta_jugada},
                          self.usuarios[data['cliente']]['socket'])
                self.actualizar_carta_central()
                self.accion = 'botar carta'
            elif data['detalles'][0] == 'mazo':
                carta = sacar_cartas(1)[0]
                self.usuarios[data['cliente']]['cartas'].append(carta)
                self.enviar_carta(carta, self.usuarios[data['cliente']]['socket'])
                self.accion = 'sacar carta'
            for usuario in self.usuarios:
                self.update_cartas_contrincantes(usuario)
            self.turno = next(self.ciclo)
            self.accion = None
            self.update_datos_pantalla()

