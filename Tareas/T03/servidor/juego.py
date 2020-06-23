
import json

with open('parametros.json') as file:
    data = json.load(file)

class Juego:

    def __init__(self):
        self.usuarios = dict()
        self.lista_usuarios = list()
        self.cantidad_jugadores = data['cantidad_jugadores']

    def usuario_valido(self, user, socket):
        if user.isalnum() and user not in self.usuarios and len(self.lista_usuarios) < self.cantidad_jugadores:
            self.usuarios[user] = {'nombre_usuario': user, 'socket': socket}
            self.lista_usuarios.append(user)
            return True
        else:
            return False

