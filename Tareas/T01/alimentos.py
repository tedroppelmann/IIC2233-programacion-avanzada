
from abc import ABC, abstractmethod
import parametros as p
import random

class Alimento(ABC):

    def __init__(self, nombre, efecto_salud, precio):
        self.nombre = nombre
        self.efecto_salud = int(efecto_salud)
        self.precio = int(precio)

    @abstractmethod
    def particularidad_alimento(self, criatura):
        pass

class TartaDeMelaza(Alimento):

    def particularidad_alimento(self, criatura):
        if criatura.tipo == "Niffler":
            if random.random() < p.PROB_CAMBIO_ARISCA_INOFENSIVA:
                print(f"¡Enhorabuena! Gacias a la Tarta de Melaza lograste disminuir la "
                      f"agresividad de {criatura.nombre} de arisca a "
                      f"inofensiva de forma permanente.")
                criatura.nivel_agresividad = "inofensiva"
        criatura.nivel_hambre = "satisfecha"

class HigadoDeDragon(Alimento):

    def particularidad_alimento(self, criatura):
        if criatura.estado_salud:
            criatura.estado_salud = False
            print(f"Gracias al Hígado de Dragón, {criatura.nombre} ha sanado.")
        else:
            print(f"{criatura.nombre} ya está sana por lo que el Hígado de Dragón solo "
                  f"aporta en su salud actual.")
        criatura.nivel_hambre = "satisfecha"

class BuenueloDeGusarajo(Alimento):

    def particularidad_alimento(self, criatura):
        if random.random() < p.PROB_RECHAZAR_BUNUELO:
            print(f"{criatura.nombre} ha rechazdo tu Buñuelo de Gusarajo")
            criatura.salud_actual -= self.efecto_salud
        else:
            print(f"{criatura.nombre} acepto tu Buñuelo de Gusarajo, a pesar de su mal sabor.")
            criatura.nivel_hambre = "satisfecha"
            return False

