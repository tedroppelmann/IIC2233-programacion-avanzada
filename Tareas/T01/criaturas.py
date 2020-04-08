
from magizoologos import Personajes
import parametros as p

class Criaturas(Personajes):

    def __init__(self, nombre, tipo, nivel_magico, probabilidad_escape, probabilidad_enfermarse,
                 estado_salud, estado_escape, salud_total, salud_actual, nivel_hambre,
                 nivel_agresividad, dias_sin_comer, nivel_cleptomania):

        super().__init__(nombre, tipo, nivel_magico)
        self.probabilidad_escape = probabilidad_escape
        self.probabilidad_enfermarse = probabilidad_enfermarse
        self.estado_salud = estado_salud
        self.estado_escape = estado_escape
        self.salud_total = salud_total
        self.salud_actual = salud_actual
        self.nivel_hambre = nivel_hambre
        self.nivel_agresividad = nivel_agresividad
        self.dias_sin_comer = dias_sin_comer
        self.nivel_cleptomania = nivel_cleptomania
        self.precio = None

class Augurey(Criaturas):

    def __init__(self, nombre, tipo, nivel_magico, probabilidad_escape, probabilidad_enfermarse,
                 estado_salud, estado_escape, salud_total, salud_actual, nivel_hambre,
                 nivel_agresividad, dias_sin_comer, nivel_cleptomania):

        super().__init__(nombre, tipo, nivel_magico, probabilidad_escape, probabilidad_enfermarse,
                 estado_salud, estado_escape, salud_total, salud_actual, nivel_hambre,
                 nivel_agresividad, dias_sin_comer, nivel_cleptomania)
        self.precio = p.PRECIO_AUGEREY

class Niffler(Criaturas):

    def __init__(self, nombre, tipo, nivel_magico, probabilidad_escape, probabilidad_enfermarse,
                 estado_salud, estado_escape, salud_total, salud_actual, nivel_hambre,
                 nivel_agresividad, dias_sin_comer, nivel_cleptomania):

        super().__init__(nombre, tipo, nivel_magico, probabilidad_escape, probabilidad_enfermarse,
                 estado_salud, estado_escape, salud_total, salud_actual, nivel_hambre,
                 nivel_agresividad, dias_sin_comer, nivel_cleptomania)
        self.precio = p.PRECIO_NIFFLER

class Erkling(Criaturas):

    def __init__(self, nombre, tipo, nivel_magico, probabilidad_escape, probabilidad_enfermarse,
                 estado_salud, estado_escape, salud_total, salud_actual, nivel_hambre,
                 nivel_agresividad, dias_sin_comer, nivel_cleptomania):

        super().__init__(nombre, tipo, nivel_magico, probabilidad_escape, probabilidad_enfermarse,
                 estado_salud, estado_escape, salud_total, salud_actual, nivel_hambre,
                 nivel_agresividad, dias_sin_comer, nivel_cleptomania)
        self.precio = p.PRECIO_ERKLING