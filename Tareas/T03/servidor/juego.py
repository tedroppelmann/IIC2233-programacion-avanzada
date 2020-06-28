
import json
from generador_de_mazos import sacar_cartas

with open('parametros.json') as file:
    data = json.load(file)

class Juego:

    def __init__(self):
        self.usuarios = dict()
        self.lista_usuarios = list()
        self.cantidad_jugadores = data['cantidad_jugadores']
        self.carta_jugada = None

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


