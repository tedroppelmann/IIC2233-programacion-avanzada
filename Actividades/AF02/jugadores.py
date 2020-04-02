from abc import ABC, abstractmethod
import random


class Jugador(ABC):

    def __init__(self, nombre, equipo, especialidad, energia):
        # Completar
        self.nombre = nombre
        self.equipo = equipo
        self.especialidad = especialidad
        self.energia = energia
        self.inteligencia = None
        self.audacia = None
        self.trampa = None
        self.nerviosismo = None

    def __str__(self):
        if self.equipo == 'ayudante':
            return f'Ayudante {self.nombre} ({self.especialidad})'
        return f'Alumno(a) {self.nombre} ({self.especialidad})'
    
    def __repr__(self):
        return (f'({type(self).__name__}) {self.nombre}: '
                f'equipo={self.equipo}|'
                f'energia={self.energia}|'
                f'inteligencia={self.inteligencia}|'
                f'audacia={self.audacia}|'
                f'trampa={self.trampa}|'
                f'nerviosismo={self.nerviosismo}')

    @abstractmethod
    def enfrentar(self, tipo_de_juego, enemigo):
        if self.equipo == 'ayudante':
            print(f"Ayudante {self.nombre} ({self.especialidad}): ¡Desafío a Alumno(a) "
                  f"{enemigo.nombre} ({enemigo.especialidad}) a un juego de {tipo_de_juego}!")
        elif self.equipo == 'alumno':
            print(f"Alumno(a) {self.nombre} ({self.especialidad}): ¡Desafío a Ayudante "
                  f"{enemigo.nombre} ({enemigo.especialidad}) a un juego de {tipo_de_juego}!")









# Completar la siguiente clase.
# Puedes agregarle herencia.
# Puedes agregar métodos incluso.
class JugadorMesa(Jugador):

    def __init__(self, nombre, equipo, especialidad, energia):
        # Completar 
        # ¡Aprovecha herencia!
        super().__init__(nombre, equipo, especialidad, energia)
        self.inteligencia = 3
        self.audacia = 3
        self.trampa = 3
        self.nerviosismo = min(int(self.energia), int(random.randint(0, 3)))


    def jugar_mesa(self, enemigo):
        # Completar
        if int(enemigo.nerviosismo) > int(self.nerviosismo):
            return True
        elif int(enemigo.nerviosismo) <= int(self.nerviosismo):
            return False

    def enfrentar(self, tipo_de_juego, enemigo):
        # Completar
        super().enfrentar(tipo_de_juego, enemigo)
        self.jugar_mesa(enemigo)



# Completar la siguiente clase.
# Puedes agregarle herencia.
# Puedes agregar métodos incluso.
class JugadorCartas(Jugador):

    def __init__(self, nombre, equipo, especialidad, energia):
        # Completar 
        # ¡Aprovecha herencia!
        super().__init__(nombre, equipo, especialidad, energia)
        self.audacia = 3
        self.trampa = 3
        self.nerviosismo = 3
        self.inteligencia = int(self.energia) * 2.5



    def jugar_cartas(self, enemigo):
        # Completar
        if int(enemigo.inteligencia) >= int(self.inteligencia):
            return False
        elif int(enemigo.inteligencia) < int(self.inteligencia):
            return True

    def enfrentar(self, tipo_de_juego, enemigo):
        # Completar
        super().enfrentar(tipo_de_juego, enemigo)
        self.jugar_cartas(enemigo)

# Completar la siguiente clase.
# Puedes agregarle herencia.
# Puedes agregar métodos incluso.
class JugadorCombate(Jugador):

    def __init__(self, nombre, equipo, especialidad, energia):
        # Completar 
        # ¡Aprovecha herencia!
        super().__init__(nombre, equipo, especialidad, energia)
        self.inteligencia = 3
        self.trampa = 3
        self.nerviosismo = 3
        self.audacia = int(max(int(self.energia), int(random.randint(3, 5))))


    def jugar_combate(self, enemigo):
        # Completar
        if int(enemigo.audacia) < int(self.audacia):
            return True
        elif int(enemigo.audacia) >= int(self.audacia):
            return False

    def enfrentar(self, tipo_de_juego, enemigo):
        # Completar
        super().enfrentar(tipo_de_juego, enemigo)
        self.jugar_combate(enemigo)


# Completar la siguiente clase.
# Puedes agregarle herencia.
# Puedes agregar métodos incluso.
class JugadorCarreras(Jugador):

    def __init__(self, nombre, equipo, especialidad, energia):
        # Completar 
        # ¡Aprovecha herencia!
        super().__init__(nombre, equipo, especialidad, energia)
        self.audacia = 3
        self.inteligencia = 3
        self.nerviosismo = 3
        self.trampa = int(self.energia) * 3


    def jugar_carrera(self, enemigo):
        # Completar
        if int(enemigo.trampa) < int(self.trampa):
            return True
        elif int(enemigo.trampa) >= int(self.trampa):
            return False

    def enfrentar(self, tipo_de_juego, enemigo):
        # Completar
        super().enfrentar(tipo_de_juego, enemigo)
        self.jugar_carrera(enemigo)

# Completar la siguiente clase.
# Puedes agregarle herencia.
# Puedes agregar métodos incluso.
class JugadorInteligente(JugadorMesa, JugadorCartas):

    def __init__(self, nombre, equipo, especialidad, energia):
        # Completar 
        # ¡Aprovecha herencia!
        super().__init__(nombre, equipo, especialidad, energia)
        self.audacia = 3
        self.inteligencia = 3
        self.nerviosismo = min(int(self.energia), int(random.randint(0, 3)))
        self.inteligencia = int(self.energia) * 2.5

    def enfrentar(self, tipo_de_juego, enemigo):
        # Completar
        super().enfrentar(tipo_de_juego, enemigo)
        if tipo_de_juego == "mesa":
            self.jugar_mesa(enemigo)
        elif tipo_de_juego == "cartas":
            self.jugar_cartas(enemigo)



# Completar la siguiente clase.
# Puedes agregarle herencia.
# Puedes agregar métodos incluso.
class JugadorIntrepido(JugadorCombate, JugadorCarreras):

    def __init__(self, nombre, equipo, especialidad, energia):
        # Completar 
        # ¡Aprovecha herencia!
        super().__init__(nombre, equipo, especialidad, energia)
        self.nerviosismo = 3
        self.inteligencia = 3
        self.audacia = max(int(self.energia), int(random.randint(3, 5)))
        self.trampa = self.energia * 3

    def enfrentar(self, tipo_de_juego, enemigo):
        # Completar
        super().enfrentar(tipo_de_juego, enemigo)
        if tipo_de_juego == "combate":
            self.jugar_combate(enemigo)
        elif tipo_de_juego == "carreras":
            self.jugar_carrera(enemigo)