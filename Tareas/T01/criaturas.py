
import parametros as p
import random
from abc import ABC, abstractmethod
from actualizaciones import actualizar_datos_magizoologo, actualizar_datos_criaturas, str_bool

class Criatura(ABC):

    def __init__(self, nombre, tipo, nivel_magico, probabilidad_escape, probabilidad_enfermarse,
                 estado_salud, estado_escape, salud_total, salud_actual, nivel_hambre,
                 nivel_agresividad, dias_sin_comer, nivel_cleptomania):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel_magico = int(nivel_magico)
        self.probabilidad_escape = probabilidad_escape
        self.probabilidad_enfermarse = probabilidad_enfermarse
        self.estado_salud = str_bool(estado_salud)
        self.estado_escape = str_bool(estado_escape)
        self.salud_total = int(salud_total)
        self.salud_actual = int(salud_actual)
        self.nivel_hambre = nivel_hambre
        self.nivel_agresividad = nivel_agresividad
        self.dias_sin_comer = int(dias_sin_comer)
        self.nivel_cleptomania = nivel_cleptomania
        self.precio = None

    def alimentarse(self, DCC):
        if self.nivel_hambre == "satisfecha":
            efecto_hambre = p.EFECTO_HAMBRE_SATISFECHA
        else:
            efecto_hambre = p.EFECTO_HAMBRE_HAMBRIENTA

        if self.nivel_agresividad == "inofensiva":
            efecto_agresividad = p.EFECTO_AGRESIVIDAD_INOFENSIVA
        elif self.nivel_agresividad == "arisca":
            efecto_agresividad = p.EFECTO_AGRESIVIDAD_ARISCA
        else:
            efecto_agresividad = p.EFECTO_AGRESIVIDAD_PELIGROSA

        prob_ataque = min(1, (efecto_hambre + efecto_agresividad)/100)
        prob = random.random()
        if prob <= prob_ataque:
            puntos_perdidos = max(10, DCC.usuario_actual.nivel_magico - self.nivel_magico)
            print(f"¡{self.nombre} te ha atacado! Has perdido {puntos_perdidos} puntos de energía.")
            return puntos_perdidos
        else:
            print("¡No hubo ataque de la DCCriatura!")
            return 0


class Augurey(Criatura):

    def __init__(self, nombre, tipo, nivel_magico, probabilidad_escape, probabilidad_enfermarse,
                 estado_salud, estado_escape, salud_total, salud_actual, nivel_hambre,
                 nivel_agresividad, dias_sin_comer, nivel_cleptomania):

        super().__init__(nombre, tipo, nivel_magico, probabilidad_escape, probabilidad_enfermarse,
                 estado_salud, estado_escape, salud_total, salud_actual, nivel_hambre,
                 nivel_agresividad, dias_sin_comer, nivel_cleptomania)
        self.precio = p.PRECIO_AUGEREY



class Niffler(Criatura):

    def __init__(self, nombre, tipo, nivel_magico, probabilidad_escape, probabilidad_enfermarse,
                 estado_salud, estado_escape, salud_total, salud_actual, nivel_hambre,
                 nivel_agresividad, dias_sin_comer, nivel_cleptomania):
        super().__init__(nombre, tipo, nivel_magico, probabilidad_escape, probabilidad_enfermarse,
                 estado_salud, estado_escape, salud_total, salud_actual, nivel_hambre,
                 nivel_agresividad, dias_sin_comer, nivel_cleptomania)
        self.precio = p.PRECIO_NIFFLER




class Erkling(Criatura):

    def __init__(self, nombre, tipo, nivel_magico, probabilidad_escape, probabilidad_enfermarse,
                 estado_salud, estado_escape, salud_total, salud_actual, nivel_hambre,
                 nivel_agresividad, dias_sin_comer, nivel_cleptomania):

        super().__init__(nombre, tipo, nivel_magico, probabilidad_escape, probabilidad_enfermarse,
                 estado_salud, estado_escape, salud_total, salud_actual, nivel_hambre,
                 nivel_agresividad, dias_sin_comer, nivel_cleptomania)
        self.precio = p.PRECIO_ERKLING

