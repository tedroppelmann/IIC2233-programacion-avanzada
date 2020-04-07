
import sys
from DCC import Dcc
from cargas import cargar_magizoologos, cargar_criaturas, cargar_alimentos

class Juego:

    def __init__(self):
        self.dias = 1

    def iniciar(self):
        magizoologos = cargar_magizoologos("magizoologos.csv")
        criaturas = cargar_criaturas("criaturas.csv")
        alimentos = cargar_alimentos("alimentos.csv")
        DCC = Dcc(magizoologos, criaturas, alimentos)
        while True:
            print("***** MENÚ DE INICIO *****")
            print("Selecciones una opción:")
            print("[1] Crear Magizoólogo")
            print("[2] Cargar Magizoólogo")
            print("[0] Salir")
            respuesta = input("Indique una opción (1, 2 o 0):")
            if respuesta == "1":
                DCC.crear_magizoologo()
            elif respuesta == "2":
                DCC.cargar_magizoologo()
            elif respuesta == "0":
                print("Adiós ¡Vuelve pronto!")
                sys.exit()
            else:
                print("ERROR. Intente nuevamente.")


if __name__ == "__main__":
    print("***** ¡Bienvenido a DCCriaturas Fantásticas! ***** \n")
    juego = Juego()
    juego.iniciar()