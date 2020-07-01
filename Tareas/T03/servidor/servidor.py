
import socket
import threading
import json
import base64
import time
from generador_de_mazos import sacar_cartas
import random

with open('parametros.json') as file:
    parametros = json.load(file)

lock_global = threading.Lock()

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
        self.ciclo = Turnos()
        self.cantidad_jugadores = parametros['cantidad_jugadores']
        self.carta_jugada = None
        self.turno = None
        self.accion = None
        self.suma = 0
        self.jugando = True
        self.eliminado = None
        self.carta_color_especial = None
        self.color = False
        self.ganador = None
        self.fin = False

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
                self.ciclo.agregar(data['cliente'])
                response['usuarios_conectados'] = self.ciclo.lista
                self.update_sala_espera(response)
            else:
                response['detalles'] = 'rechazado'
                self.send(response, client_socket)

        elif data['evento'] == 'cerrar':
            response['evento'] = 'cerrar'
            self.ciclo.eliminar(data['cliente'])
            del self.usuarios[data['cliente']]
            response['usuarios_conectados'] = self.ciclo.lista
            self.update_sala_espera(response)

        elif data['evento'] == 'empezar':
            self.enviar_carta(('reverso', 'reverso'), self.usuarios[data['cliente']]['socket'])
            self.empezar += 1
            self.poblar_cartas(data['cliente'])
            for carta in self.usuarios[data['cliente']]['cartas']:
                self.enviar_carta(carta, client_socket)
            time.sleep(0.5)
            self.update_cartas_contrincantes(data['cliente'])
            with lock_global:
                if self.empezar == self.cantidad_jugadores:
                    if self.carta_jugada is None:
                        print('Juego listo para empezar')
                        self.accion = 'ROBA 1 CARTA'
                        self.turno = self.ciclo.lista[0]
                        print(f'Es el turno de {self.turno}')
                        print(self.ciclo.lista)
                        self.usuarios[self.turno]['jugando'] = True
                        carta = sacar_cartas(1)[0]
                        self.carta_jugada = carta
                        # envío la primera carta a todos los usuarios
                        self.actualizar_carta_central()
                        if self.carta_jugada[0] == '+2':
                            self.suma += 2
                            self.accion = 'ROBA 2 CARTAS'
                        elif self.carta_jugada[0] == 'sentido':
                            self.ciclo.invertir()
                        elif self.carta_jugada[0] == 'color':
                            colores = random.choice(['amarillo', 'azul', 'rojo', 'verde'])
                            self.carta_jugada = ('color', colores)
                            self.carta_color_especial = colores
                        self.update_datos_pantalla()

        elif data['evento'] == 'jugar carta' or data['evento'] == 'sacar carta mazo':
            self.jugar_turno(data)

        elif data['evento'] == 'color seleccionado':
            self.usuarios[self.turno]['jugando'] = False
            self.turno = self.ciclo.count()
            self.color = False
            self.accion = 'ROBA 1 CARTA'
            self.carta_color_especial = data['detalles']
            self.update_datos_pantalla()
            self.carta_color_especial = None

            self.carta_jugada = ('color', data['detalles'])
            self.send({'cliente': data['cliente'],
                       'evento': 'eliminar carta',
                       'detalles': ('color', '')},
                      self.usuarios[data['cliente']]['socket'])
            self.actualizar_carta_central()
            self.usuarios[self.turno]['jugando'] = True

        elif data['evento'] == 'reiniciar':
            self.reiniciar_datos()

        elif data['evento'] == 'gritar':
            with lock_global:
                print(f'ACTIVADO POR {data["cliente"]}')
                i = 0
                for usuario in self.usuarios:
                    if self.usuarios[usuario]['uno']:
                        if data['cliente'] == usuario:
                            print('Bien. Gritaste antes que los otros. No se te suman cartas')
                        else:
                            print('Alguien gritó antes. Se suman 4 cartas')
                            for i in range(0, parametros['cartas_penitencia']):
                                carta = sacar_cartas(1)[0]
                                self.usuarios[usuario]['cartas'].append(carta)
                                self.enviar_carta(carta, self.usuarios[usuario]['socket'])

                            if self.cantidad_cartas(data['cliente']) >= parametros['cartas_maximas']:
                                print(f'{data["cliente"]} superó el máximo de cartas')
                                self.usuarios[data['cliente']]['cartas'].clear()
                                self.send({'cliente': data['cliente'],
                                           'evento': 'perdedor',
                                           'detalles': '-'},
                                          self.usuarios[data['cliente']]['socket'])
                                self.ciclo.eliminar(data['cliente'])

                        self.usuarios[data['cliente']]['uno'] = False
                        i += 1
                if i == 0:
                    for i in range(0, parametros['cartas_penitencia']):
                        carta = sacar_cartas(1)[0]
                        self.usuarios[data['cliente']]['cartas'].append(carta)
                        self.enviar_carta(carta, self.usuarios[data['cliente']]['socket'])
                    if self.cantidad_cartas(data['cliente']) >= parametros['cartas_maximas']:
                        print(f'{data["cliente"]} superó el máximo de cartas')
                        self.usuarios[data['cliente']]['cartas'].clear()
                        self.send({'cliente': data['cliente'],
                                   'evento': 'perdedor',
                                   'detalles': '-'}, self.usuarios[data['cliente']]['socket'])
                        self.ciclo.eliminar(data['cliente'])
                        if data['cliente'] == self.turno:
                            self.usuarios[self.turno]['jugando'] = False
                            self.turno = self.ciclo.count()
                            self.usuarios[self.turno]['jugando'] = True
                            self.ciclo.contador -= 1
                        self.ciclo.count()
                for user in self.usuarios:
                    self.update_cartas_contrincantes(user)
                self.update_datos_pantalla()
                print(self.ciclo.lista)
                print(self.turno)
                print(self.ciclo.contador)

    def actualizar_carta_central(self):
        for usuario in self.usuarios:
            self.send({'evento': 'actualizar carta central'},
                      self.usuarios[usuario]['socket'])
            self.enviar_carta(self.carta_jugada,
                              self.usuarios[usuario]['socket'])
            self.send({'evento': 'actualizar carta central_2'},
                      self.usuarios[usuario]['socket'])

    def update_sala_espera(self, response):
        for usuario in self.ciclo.lista:
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
        mensaje['usuarios_conectados'] = self.ciclo.lista
        for usuario in self.usuarios:
            print(f'Usuario a actualizar contrincantes: {usuario}')
            cartas = self.cantidad_cartas(usuario)
            mensaje['cliente'] = usuario
            mensaje['detalles'] = cartas
            if usuario != user:
                self.send(mensaje, self.usuarios[user]['socket'])

    def update_datos_pantalla(self):
        mensaje = dict()
        mensaje['evento'] = 'actualizar datos pantalla'
        for usuario in self.usuarios:
            mensaje['cliente'] = usuario
            mensaje['turno'] = self.turno
            mensaje['accion'] = self.accion
            mensaje['color'] = self.carta_color_especial
            self.send(mensaje, self.usuarios[usuario]['socket'])

    def usuario_valido(self, user, socket):
        if user.isalnum() and user not in self.usuarios and len(self.ciclo.lista) < self.cantidad_jugadores:
            self.usuarios[user] = {'nombre_usuario': user,
                                   'socket': socket,
                                   'cartas': [],
                                   'jugando': False,
                                   'uno': False}
            return True
        else:
            return False

    def poblar_cartas(self, usuario):
        self.usuarios[usuario]['cartas'] = sacar_cartas(parametros['cartas_iniciales'])
        print(self.usuarios[usuario]['nombre_usuario'],self.usuarios[usuario]['cartas'])
        # agregamos la primera carta en juego

    def cantidad_cartas(self, usuario):
        return len(self.usuarios[usuario]['cartas'])

    def jugar_turno(self, data):
        print(f'Es el turno de: {self.turno}')
        if self.turno == data['cliente']:
            print('JUGADOR VALIDO')
            self.eliminado = False
            numero = data['detalles'][0]
            color = data['detalles'][1]
            if self.usuarios[self.turno]['jugando']:
                if self.carta_jugada[0] == '+2' and self.suma > 0:
                    if self.carta_jugada[0] == numero:
                        self.carta_jugada = (numero, color)
                        self.usuarios[data['cliente']]['cartas'].remove(self.carta_jugada)
                        self.send({'cliente': data['cliente'],
                                   'evento': 'eliminar carta',
                                   'detalles': self.carta_jugada},
                                  self.usuarios[data['cliente']]['socket'])
                        self.actualizar_carta_central()
                        self.suma += 2
                        self.accion = f'ROBA {self.suma} CARTAS'
                        self.usuarios[self.turno]['jugando'] = False

                    elif data['detalles'][0] == 'mazo':
                        for i in range(0, self.suma):
                            carta = sacar_cartas(1)[0]
                            self.usuarios[data['cliente']]['cartas'].append(carta)
                            self.enviar_carta(carta, self.usuarios[data['cliente']]['socket'])
                        self.accion = 'ROBA 1 CARTA'
                        self.suma = 0
                        self.usuarios[self.turno]['jugando'] = False

                elif numero == 'color':
                    self.send({'cliente':data['cliente'],
                               'evento': 'activar carta color',
                               'detalles': '-'}, self.usuarios[data['cliente']]['socket'])
                    self.color = True
                    self.usuarios[data['cliente']]['cartas'].remove(('color',''))

                else:
                    if self.carta_jugada[0] == numero or self.carta_jugada[1] == color:

                        if numero == 'sentido':
                            self.ciclo.invertir()

                        self.carta_jugada = (numero, color)
                        self.usuarios[data['cliente']]['cartas'].remove(self.carta_jugada)
                        self.send({'cliente': data['cliente'],
                                   'evento': 'eliminar carta',
                                   'detalles': self.carta_jugada},
                                  self.usuarios[data['cliente']]['socket'])
                        self.actualizar_carta_central()
                        self.accion = 'ROBA 1 CARTA'
                        self.usuarios[self.turno]['jugando'] = False
                        if numero == '+2':
                            self.suma += 2
                            self.accion = f'ROBA {self.suma} CARTAS'

                    elif data['detalles'][0] == 'mazo':
                        carta = sacar_cartas(1)[0]
                        self.usuarios[data['cliente']]['cartas'].append(carta)
                        self.enviar_carta(carta, self.usuarios[data['cliente']]['socket'])
                        self.accion = 'ROBA 1 CARTA'
                        self.usuarios[self.turno]['jugando'] = False

                if self.cantidad_cartas(self.turno) >= parametros['cartas_maximas']:
                    print(f'{self.turno} superó el máximo de cartas')
                    self.usuarios[self.turno]['cartas'].clear()
                    self.send({'cliente': self.turno,
                               'evento': 'perdedor',
                               'detalles': '-'}, self.usuarios[self.turno]['socket'])
                    for usuario in self.usuarios:
                        print(f'usuarios eliminados: {usuario}')
                        self.update_cartas_contrincantes(usuario)
                    self.ciclo.eliminar(self.turno)
                    self.eliminado = True

                if len(self.usuarios[self.turno]['cartas']) == 1:
                    print('Te queda una carta')
                    self.usuarios[self.turno]['uno'] = True

                if self.ciclo.largo == 1:
                    print('Hay un ganador')
                    self.ganador = self.ciclo.lista[0]
                    self.enviar_ganador()

                if len(self.usuarios[self.turno]['cartas']) == 0 and self.turno in self.ciclo.lista:
                    print('Hay un ganador')
                    self.ganador = self.turno
                    self.enviar_ganador()

                if not self.usuarios[self.turno]['jugando'] and not self.color and not self.fin:
                    if not self.eliminado:
                        print(self.usuarios)
                        for usuario in self.usuarios:
                            self.update_cartas_contrincantes(usuario)
                    self.jugando = True
                    print(self.ciclo.lista)
                    self.turno = self.ciclo.count()
                    print(f'es el turno de {self.turno}')
                    print(self.ciclo.contador)
                    self.usuarios[self.turno]['jugando'] = True
                    self.update_datos_pantalla()

    def enviar_ganador(self):
        self.send({'cliente': self.ganador,
                   'evento': 'fin del juego',
                   'detalles': 'ganador'},
                  self.usuarios[self.ganador]['socket'])
        for usuario in self.usuarios:
            if usuario != self.ganador:
                self.send({'cliente': usuario,
                           'evento': 'fin del juego',
                           'detalles': 'perdedor'},
                          self.usuarios[usuario]['socket'])
        self.fin = True

    def reiniciar_datos(self):
        self.empezar = 0
        self.usuarios = dict()
        self.ciclo = Turnos()
        self.carta_jugada = None
        self.turno = None
        self.accion = None
        self.suma = 0
        self.jugando = True
        self.eliminado = None
        self.carta_color_especial = None
        self.color = False
        self.ganador = None
        self.fin = False

class Turnos:

    def __init__(self):
        self.lista = list()
        self.contador = 0
        self.largo = 0

    def agregar(self, usuario):
        self.lista.append(usuario)
        self.largo += 1

    def largo(self):
        return len(self.lista)

    def count(self):
        if self.contador < self.largo - 1:
            self.contador += 1
        elif self.contador == self.largo - 1:
            self.contador = 0
        return self.lista[self.contador]

    def eliminar(self, usuario):
        self.lista.remove(usuario)
        self.largo -= 1
        if self.contador > 0:
            self.contador -= 1
        elif self.contador == 0:
            self.contador = self.largo - 1

    def invertir(self):
        usuario = self.lista[self.contador]
        invertida = self.lista[::-1]
        self.lista = invertida
        while self.lista[self.contador] != usuario:
            self.count()