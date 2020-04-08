
import sys
from DCC import Dcc
from cargas import cargar_magizoologos, cargar_criaturas, cargar_alimentos
from menus import  menu_inicio

class Juego:

    def __init__(self):
        self.dias = 1

    def iniciar(self):
        magizoologos = cargar_magizoologos("magizoologos.csv")
        criaturas = cargar_criaturas("criaturas.csv")
        alimentos = cargar_alimentos("alimentos.csv")
        DCC = Dcc(magizoologos, criaturas, alimentos, usuario_actual=None)
        menu_inicio(DCC)


if __name__ == "__main__":
    print("***** ¡Bienvenido a DCCriaturas Fantásticas! ***** \n")
    juego = Juego()
    juego.iniciar()