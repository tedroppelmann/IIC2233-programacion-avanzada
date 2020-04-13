
import parametros as p
import random
from abc import ABC, abstractmethod
from actualizaciones import str_bool

class Criatura(ABC):

    def __init__(self, nombre, tipo, nivel_magico, probabilidad_escape, probabilidad_enfermarse,
                 estado_salud, estado_escape, salud_total, salud_actual, nivel_hambre,
                 nivel_agresividad, dias_sin_comer, nivel_cleptomania):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel_magico = int(nivel_magico)
        self.probabilidad_escape = float(probabilidad_escape)
        self.probabilidad_enfermarse = float(probabilidad_enfermarse)
        self.estado_salud = str_bool(estado_salud)
        self.estado_escape = str_bool(estado_escape)
        self.__salud_total = int(salud_total)
        self.__salud_actual = int(salud_actual)
        self.nivel_hambre = nivel_hambre
        self.nivel_agresividad = nivel_agresividad
        self.dias_sin_comer = int(dias_sin_comer)
        self.nivel_cleptomania = int(nivel_cleptomania)

        self.comio_hoy = False
        self.precio = None

    @property
    def salud_actual(self):
        return self.__salud_actual

    @salud_actual.setter
    def salud_actual(self, k):
        if k > self.salud_total:
            self.__salud_actual = self.salud_total
        elif k < p.SALUD_MINIMA:
            self.__salud_actual = p.SALUD_MINIMA
        else:
            self.__salud_actual = k

    @property
    def salud_total(self):
        return self.__salud_total

    @salud_total.setter
    @abstractmethod
    def salud_total(self, k):
        pass

    def alimentarse(self, dcc):
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
            puntos_perdidos = max(10, dcc.usuario_actual.nivel_magico - self.nivel_magico)
            print(f"¡{self.nombre} te ha atacado! Has perdido {puntos_perdidos} puntos de energía.")
            dcc.usuario_actual.energia_actual -= puntos_perdidos
        else:
            print("¡No hubo ataque de la DCCriatura!")


    def escaparse(self, dcc):
        if not self.estado_escape:
            efecto_hambre = p.EFECTO_HAMBRE_MIN_ESCAPARSE
            if self.nivel_hambre == "hambrienta":
                efecto_hambre = p.EFECTO_HAMBRE_MAX_ESCAPARSE
            prob_escape = min(1, self.probabilidad_escape + max(0,(efecto_hambre - dcc.usuario_actual.responsabilidad) / 100))
            if random.random() < prob_escape:
                self.estado_escape = True
                return self

    def enfermarse(self, dcc):
        if not self.estado_salud:
            prob_enfermarse = min(1, self.probabilidad_enfermarse + max(0, ((self.salud_total - self.salud_actual)/self.salud_total - (dcc.usuario_actual.responsabilidad/100))))
            if random.random() < prob_enfermarse:
                self.estado_salud = True
                return self

    @abstractmethod
    def cambiar_hambre(self):
        pass

    def habilidad_comienzo_dia(self, dcc):
        pass

class Augurey(Criatura):

    def __init__(self, nombre, tipo, nivel_magico, probabilidad_escape, probabilidad_enfermarse,
                 estado_salud, estado_escape, salud_total, salud_actual, nivel_hambre,
                 nivel_agresividad, dias_sin_comer, nivel_cleptomania):

        super().__init__(nombre, tipo, nivel_magico, probabilidad_escape, probabilidad_enfermarse,
                 estado_salud, estado_escape, salud_total, salud_actual, nivel_hambre,
                 nivel_agresividad, dias_sin_comer, nivel_cleptomania)
        self.precio = p.PRECIO_AUGEREY

    @Criatura.salud_total.setter
    def salud_total(self, k):
        if k > p.SALUD_AUGUREY_MAX:
            self.__salud_total = p.SALUD_AUGUREY_MAX
        else:
            self.__salud_total = k

    def cambiar_hambre(self):
        if self.nivel_hambre == "satisfecha":
            if self.dias_sin_comer >= p.DIAS_SIN_COMER_AUGUREY:
                self.nivel_hambre = "hambrienta"
                return self

    def habilidad_comienzo_dia(self, dcc):
        if self.nivel_hambre == "satisfecha" and not self.estado_salud and self.salud_actual == self.salud_total:
            ofrenda = random.choice(["Tarta de Melaza", "Hígado de Dragón",
                                        "Buñuelo de Gusarajo"])
            print(f"¡Tu Augurey {self.nombre} te ha traído como ofrenda un un(a) {ofrenda}!")
            dcc.usuario_actual.alimentos.append(ofrenda)

class Niffler(Criatura):

    def __init__(self, nombre, tipo, nivel_magico, probabilidad_escape, probabilidad_enfermarse,
                 estado_salud, estado_escape, __salud_total, salud_actual, nivel_hambre,
                 nivel_agresividad, dias_sin_comer, nivel_cleptomania):
        super().__init__(nombre, tipo, nivel_magico, probabilidad_escape, probabilidad_enfermarse,
                 estado_salud, estado_escape, __salud_total, salud_actual, nivel_hambre,
                 nivel_agresividad, dias_sin_comer, nivel_cleptomania)
        self.precio = p.PRECIO_NIFFLER

    @Criatura.salud_total.setter
    def salud_total(self, k):
        if k > p.SALUD_NIFFLER_MAX:
            self.__salud_total = p.SALUD_NIFFLER_MAX
        else:
            self.__salud_total = k

    def cambiar_hambre(self):
        if self.nivel_hambre == "satisfecha":
            if self.dias_sin_comer >= p.DIAS_SIN_COMER_NIFFLER:
                self.nivel_hambre = "hambrienta"
                return self

    def habilidad_comienzo_dia(self, dcc):
        if self.nivel_hambre == "satisfecha":
            ofrenda = self.nivel_cleptomania * 2
            print(f"¡Tu Niffler {self.nombre} te ha traído como ofrenda {ofrenda} Sickles!")
            dcc.usuario_actual.sickles += ofrenda
            print(f"Tu saldo actual es: {dcc.usuario_actual.sickles} Sickles")
        else:
            robo = self.nivel_cleptomania * 2
            print(f"¡Tu Niffler {self.nombre} te ha robado {robo} Sickles!")
            dcc.usuario_actual.sickles -= robo
            print(f"Tu saldo actual es: {dcc.usuario_actual.sickles} Sickles")

class Erkling(Criatura):

    def __init__(self, nombre, tipo, nivel_magico, probabilidad_escape, probabilidad_enfermarse,
                 estado_salud, estado_escape, __salud_total, salud_actual, nivel_hambre,
                 nivel_agresividad, dias_sin_comer, nivel_cleptomania):

        super().__init__(nombre, tipo, nivel_magico, probabilidad_escape, probabilidad_enfermarse,
                 estado_salud, estado_escape, __salud_total, salud_actual, nivel_hambre,
                 nivel_agresividad, dias_sin_comer, nivel_cleptomania)
        self.precio = p.PRECIO_ERKLING

    @Criatura.salud_total.setter
    def salud_total(self, k):
        if k > p.SALUD_ERKLING_MAX:
            self.__salud_total = p.SALUD_ERKLING_MAX
        else:
            self.__salud_total = k

    def cambiar_hambre(self):
        if self.nivel_hambre == "satisfecha":
            if self.dias_sin_comer >= p.DIAS_SIN_COMER_ERKLING:
                self.nivel_hambre = "hambrienta"
                return self

    def habilidad_comienzo_dia(self, dcc):
        if self.nivel_hambre == "hambrienta":
            if len(dcc.usuario_actual.alimentos) > 0:
                robo = random.choice(dcc.usuario_actual.alimentos)
                dcc.usuario_actual.alimentos.remove(robo)
                print(f"¡Tu Erkling {self.nombre} te ha robado un(a) {robo}! Ahora está satisfecha")
                self.comio_hoy = True
                self.dias_sin_comer = 0
                self.nivel_hambre = "satisfecha"