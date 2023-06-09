import socket
import threading
import json
import base64
import time
from generador_de_mazos import sacar_cartas
import random
from turnos import Turnos
from tabla import Tabla
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
        self.tabla = Tabla()
        self.id = 0
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

    def send(self, value, sock):
        msg = json.dumps(value)
        msg_bytes = msg.encode()
        msg_length = len(msg_bytes).to_bytes(4, byteorder='big')
        numero_validacion = 0
        msg_tipo = numero_validacion.to_bytes(4, byteorder='big')
        sock.send(msg_tipo + msg_length + msg_bytes)
        if value['evento'] == 'update cartas contrincantes':
            self.tabla.add(value['cliente receptor'],'OUT', value['evento'],
                           str(len(msg_bytes)), value)
        elif value['evento'] == 'conectarse' and self.usuarios[value['cliente']]['socket'] != sock:
            self.tabla.add(value['cliente receptor'],'OUT', value['evento'],
                           str(len(msg_bytes)), value)
        else:
            self.tabla.add(value['cliente'],'OUT', value['evento'], str(len(msg_bytes)), value)

    def listen_client_thread(self, client_socket):
        self.id += 1
        self.tabla.add(self.id, '-', 'conexión a servidor', '-', '-')
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
                    self.tabla.add(decoded['cliente'],'IN', decoded['evento'],
                                   response_length, decoded)
            except json.decoder.JSONDecodeError or ConnectionResetError:
                user = None
                for usuario in self.usuarios:
                    if self.usuarios[usuario]['socket'] == client_socket:
                        user = usuario
                if self.empezar == 0 and user is not None:
                    self.ciclo.eliminar(user)
                    del self.usuarios[user]
                    self.update_sala_espera({'cliente': user,'evento': 'cerrar', 'detalles': '-',
                                            'usuarios_conectados': self.ciclo.lista,
                                            'cantidad_jugadores': self.cantidad_jugadores})
                elif user is not None:
                    self.usuarios[user]['cartas'].clear()
                    if user == self.turno:
                        self.usuarios[self.turno]['jugando'] = False
                        self.turno = self.ciclo.count()
                        self.usuarios[self.turno]['jugando'] = True
                    if user in self.ciclo.lista:
                        self.ciclo.eliminar(user)
                    self.usuarios[user]['activo'] = False
                    for usuario in self.usuarios:
                        self.update_cartas_contrincantes(usuario)
                    self.update_datos_pantalla()
                    if self.ciclo.largo == 1:
                        self.ganador = self.ciclo.lista[0]
                        self.enviar_ganador()
                if user is not None:
                    self.tabla.add(user, '-','desconexión a servidor', '-', '-')
                break

    def analizar_mensaje(self, data, client_socket):
        response = dict()
        response['cliente'] = data['cliente']
        response['cantidad_jugadores'] = self.cantidad_jugadores
        if data['evento'] == 'conectarse':
            response['evento'] = 'conectarse'
            if self.usuario_valido(data['cliente'], client_socket):
                response['detalles'] = 'aceptado'
                self.ciclo.agregar(data['cliente'])
                response['usuarios_conectados'] = self.ciclo.lista
                self.update_sala_espera(response)
            else:
                response['detalles'] = 'rechazado'
                self.send(response, client_socket)
        elif data['evento'] == 'empezar':
            self.enviar_carta(('reverso', 'reverso'), data['cliente'])
            self.empezar += 1
            self.usuarios[data['cliente']]['cartas'] = sacar_cartas(parametros['cartas_iniciales'])
            for carta in self.usuarios[data['cliente']]['cartas']:
                self.enviar_carta(carta, data['cliente'])
            time.sleep(0.5)
            self.update_cartas_contrincantes(data['cliente'])
            with lock_global:
                if self.empezar == self.cantidad_jugadores:
                    if self.carta_jugada is None:
                        self.accion = 'ROBA 1 CARTA'
                        self.turno = self.ciclo.lista[0]
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
            self.enviar_mensaje(data['cliente'], 'eliminar carta', ('color', ''))
            self.actualizar_carta_central()
            self.usuarios[self.turno]['jugando'] = True
        elif data['evento'] == 'reiniciar':
            self.reiniciar_datos()
        elif data['evento'] == 'gritar':
            if data['cliente'] in self.ciclo.lista:
                with lock_global:
                    i = 0
                    for usuario in self.usuarios:
                        if self.usuarios[usuario]['uno'] and self.usuarios[usuario]['activo']:
                            if data['cliente'] == usuario:
                                pass
                            else:
                                for i in range(0, parametros['cartas_penitencia']):
                                    carta = sacar_cartas(1)[0]
                                    self.usuarios[usuario]['cartas'].append(carta)
                                    self.enviar_carta(carta, usuario)
                                if self.cantidad_cartas(usuario) >= parametros['cartas_maximas']:
                                    self.usuarios[usuario]['cartas'].clear()
                                    self.enviar_mensaje(usuario, 'perdedor', '-')
                                    self.ciclo.eliminar(usuario)
                            self.usuarios[usuario]['uno'] = False
                            i += 1
                    if i == 0:
                        for i in range(0, parametros['cartas_penitencia']):
                            carta = sacar_cartas(1)[0]
                            self.usuarios[data['cliente']]['cartas'].append(carta)
                            self.enviar_carta(carta, data['cliente'])
                        if self.cantidad_cartas(data['cliente']) >= parametros['cartas_maximas']:
                            self.usuarios[data['cliente']]['cartas'].clear()
                            self.enviar_mensaje(data['cliente'], 'perdedor', '-')
                            self.ciclo.eliminar(data['cliente'])
                            if data['cliente'] == self.turno:
                                self.usuarios[self.turno]['jugando'] = False
                                self.turno = self.ciclo.count()
                                self.usuarios[self.turno]['jugando'] = True
                    for user in self.usuarios:
                        self.update_cartas_contrincantes(user)
                    self.update_datos_pantalla()
                    if self.ciclo.largo == 1:
                        self.ganador = self.ciclo.lista[0]
                        self.enviar_ganador()

    def actualizar_carta_central(self):
        for usuario in self.usuarios:
            if self.usuarios[usuario]['activo']:
                self.send({'cliente': usuario, 'evento': 'actualizar carta central'},
                          self.usuarios[usuario]['socket'])
                self.enviar_carta(self.carta_jugada, usuario)
                self.send({'cliente': usuario, 'evento': 'actualizar carta central_2'},
                          self.usuarios[usuario]['socket'])

    def update_sala_espera(self, response):
        for usuario in self.ciclo.lista:
            response['cliente receptor'] = usuario
            self.send(response, self.usuarios[usuario]['socket'])

    def enviar_carta(self, carta, usuario):
        sock = self.usuarios[usuario]['socket']
        numero = carta[0]
        color = carta[1]
        if carta[0] == 'color':
            with open(f"{parametros['path_cartas']}color.png", "rb") as file:
                bytes_imagen = base64.b64encode(file.read())
        elif carta[0] == 'reverso':
            with open(f"{parametros['path_cartas']}reverso.png", "rb") as file:
                bytes_imagen = base64.b64encode(file.read())
        else:
            with open(f"{parametros['path_cartas']}{numero}_{color}.png", "rb") as file:
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
        self.tabla.add(usuario, 'OUT','enviar carta', '-',f'{numero},{color}')

    def enviar_mensaje(self, cliente, evento, detalles):
        self.send({'cliente': cliente, 'evento': evento, 'detalles': detalles},
                  self.usuarios[cliente]['socket'])

    def update_cartas_contrincantes(self, user):
        if self.usuarios[user]['activo']:
            mensaje = dict()
            mensaje['evento'] = 'update cartas contrincantes'
            mensaje['usuarios_conectados'] = self.ciclo.lista
            for usuario in self.usuarios:
                cartas = self.cantidad_cartas(usuario)
                mensaje['cliente'] = usuario
                mensaje['detalles'] = cartas
                mensaje['cliente receptor'] = user
                if usuario != user:
                    self.send(mensaje, self.usuarios[user]['socket'])

    def update_datos_pantalla(self):
        mensaje = dict()
        mensaje['evento'] = 'actualizar datos pantalla'
        for usuario in self.usuarios:
            if self.usuarios[usuario]['activo']:
                mensaje['cliente'] = usuario
                mensaje['turno'] = self.turno
                mensaje['accion'] = self.accion
                mensaje['color'] = self.carta_color_especial
                self.send(mensaje, self.usuarios[usuario]['socket'])

    def usuario_valido(self, user, socket):
        if user.isalnum() and user not in self.usuarios and \
                        self.ciclo.largo < self.cantidad_jugadores:
            self.usuarios[user] = {'nombre_usuario': user, 'socket': socket, 'cartas': [],
                                   'jugando': False, 'uno': False, 'activo': True}
            return True
        else:
            return False

    def cantidad_cartas(self, usuario):
        return len(self.usuarios[usuario]['cartas'])

    def jugar_turno(self, data):
        if self.turno == data['cliente']:
            self.eliminado = False
            numero = data['detalles'][0]
            color = data['detalles'][1]
            if self.usuarios[self.turno]['jugando']:
                if self.carta_jugada[0] == '+2' and self.suma > 0:
                    if self.carta_jugada[0] == numero:
                        self.carta_jugada = (numero, color)
                        self.usuarios[self.turno]['cartas'].remove(self.carta_jugada)
                        self.enviar_mensaje(self.turno, 'eliminar carta', self.carta_jugada)
                        self.actualizar_carta_central()
                        self.suma += 2
                        self.accion = f'ROBA {self.suma} CARTAS'
                        self.usuarios[self.turno]['jugando'] = False
                    elif data['detalles'][0] == 'mazo':
                        for i in range(0, self.suma):
                            carta = sacar_cartas(1)[0]
                            self.usuarios[self.turno]['cartas'].append(carta)
                            self.enviar_carta(carta, self.turno)
                        self.accion = 'ROBA 1 CARTA'
                        self.suma = 0
                        self.usuarios[self.turno]['jugando'] = False
                    else:
                        self.enviar_mensaje(self.turno, 'jugada invalida', '-')
                elif numero == 'color':
                    self.enviar_mensaje(self.turno, 'activar carta color', '-')
                    self.color = True
                    self.usuarios[self.turno]['cartas'].remove(('color',''))
                else:
                    if self.carta_jugada[0] == numero or self.carta_jugada[1] == color:
                        if numero == 'sentido':
                            self.ciclo.invertir()
                        self.carta_jugada = (numero, color)
                        self.usuarios[self.turno]['cartas'].remove(self.carta_jugada)
                        self.enviar_mensaje(self.turno, 'eliminar carta', self.carta_jugada)
                        self.actualizar_carta_central()
                        self.accion = 'ROBA 1 CARTA'
                        self.usuarios[self.turno]['jugando'] = False
                        if numero == '+2':
                            self.suma += 2
                            self.accion = f'ROBA {self.suma} CARTAS'
                    elif data['detalles'][0] == 'mazo':
                        carta = sacar_cartas(1)[0]
                        self.usuarios[self.turno]['cartas'].append(carta)
                        self.enviar_carta(carta, self.turno)
                        self.accion = 'ROBA 1 CARTA'
                        self.usuarios[self.turno]['jugando'] = False
                    else:
                        self.enviar_mensaje(self.turno, 'jugada invalida', '-')
                if self.cantidad_cartas(self.turno) >= parametros['cartas_maximas']:
                    self.usuarios[self.turno]['cartas'].clear()
                    self.enviar_mensaje(self.turno, 'perdedor', '-')
                    for usuario in self.usuarios:
                        self.update_cartas_contrincantes(usuario)
                    self.ciclo.eliminar(self.turno)
                    self.eliminado = True
                if len(self.usuarios[self.turno]['cartas']) == 1:
                    self.usuarios[self.turno]['uno'] = True
                if self.ciclo.largo == 1:
                    self.ganador = self.ciclo.lista[0]
                    self.enviar_ganador()
                if len(self.usuarios[self.turno]['cartas']) == 0 and self.turno in self.ciclo.lista:
                    self.ganador = self.turno
                    self.enviar_ganador()
                if not self.usuarios[self.turno]['jugando'] and not self.color and not self.fin:
                    if not self.eliminado:
                        for usuario in self.usuarios:
                            self.update_cartas_contrincantes(usuario)
                    self.jugando = True
                    self.turno = self.ciclo.count()
                    self.usuarios[self.turno]['jugando'] = True
                    self.update_datos_pantalla()

    def enviar_ganador(self):
        self.enviar_mensaje(self.ganador, 'fin del juego', 'ganador')
        for usuario in self.usuarios:
            if usuario != self.ganador and self.usuarios[usuario]['activo']:
                self.enviar_mensaje(usuario, 'fin del juego', 'perdedor')
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