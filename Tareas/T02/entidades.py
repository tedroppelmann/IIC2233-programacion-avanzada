
class Mesero:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direccion = 'down'

class Chef:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.platos_terminados = 0
        self.estado = 'principiante'

class Mesa:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Cliente:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tipo = None