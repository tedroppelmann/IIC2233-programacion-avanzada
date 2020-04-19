
from DCC import Dcc
from cargas import cargar_magizoologos, cargar_criaturas, cargar_alimentos
from menus import  menu_inicio
import parametros as p

class Juego:

    def iniciar(self):
        """
        Inicia el juego
        :return: None
        """
        magizoologos = cargar_magizoologos(p.RUTA_MAGIZOOLOGOS)
        criaturas = cargar_criaturas(p.RUTA_CRIATURAS)
        alimentos = cargar_alimentos()
        dcc = Dcc(magizoologos, criaturas, alimentos, usuario_actual=None)
        menu_inicio(dcc)

if __name__ == "__main__":
    print("***** ¡Bienvenido a DCCriaturas Fantásticas! ***** \n")
    juego = Juego()
    juego.iniciar()