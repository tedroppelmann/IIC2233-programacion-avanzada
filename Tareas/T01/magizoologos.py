
import parametros as p

class Personajes:

    def __init__(self, nombre, tipo, nivel_magico):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel_magico = nivel_magico


class Magizoologo(Personajes):

    def __init__(self, nombre, tipo, sickles, criaturas, alimentos, licencia, nivel_magico,
                 destreza, energia, responsabilidad, habilidad_especial):
        super().__init__(nombre, tipo, nivel_magico)
        self.sickles = sickles
        self.criaturas = criaturas
        self.alimentos = alimentos
        self.licencia = licencia
        self.destreza = destreza
        self.energia = energia
        self.responsabilidad = responsabilidad
        self.habilidad_especial = habilidad_especial
        self.energia_actual = None
        self.nivel_aprobacion = None

    def adoptar(self, DCC):
        if self.licencia:
            while True:
                print("¿Qué tipo de DCCriatura quieres?\n[1] Augurey\n"
                      "[2] Niffler\n[3] Erkling")
                respuesta = input("Ingrese una opción (1, 2 o 3):")
                if respuesta == "1":
                    tipo = "Augerey"
                    if self.sickles >= p.PRECIO_AUGEREY:
                        DCC.vender_criatura(tipo)
                elif respuesta == "2":
                    tipo = "Niffler"
                elif respuesta == "Erkling":
                    tipo = "Erkling"
                else:
                    print("ERROR. Intenta nuevamente.")
        else:
            print("No posees licencia, por lo que no puedes adpotar una DCCriatura.")



class Docencio(Magizoologo):

    def __init__(self, nombre, tipo, sickles, criaturas, alimentos, licencia, nivel_magico,
                 destreza, energia, responsabilidad, habilidad_especial):

        super().__init__(nombre, tipo, sickles, criaturas, alimentos, licencia, nivel_magico,
                 destreza, energia, responsabilidad, habilidad_especial)


class Tareo(Magizoologo):
    def __init__(self, nombre, tipo, sickles, criaturas, alimentos, licencia, nivel_magico,
                 destreza, energia, responsabilidad, habilidad_especial):
        super().__init__(nombre, tipo, sickles, criaturas, alimentos, licencia, nivel_magico,
                         destreza, energia, responsabilidad, habilidad_especial)

class Hibrido(Magizoologo):
    def __init__(self, nombre, tipo, sickles, criaturas, alimentos, licencia, nivel_magico,
                 destreza, energia, responsabilidad, habilidad_especial):
        super().__init__(nombre, tipo, sickles, criaturas, alimentos, licencia, nivel_magico,
                         destreza, energia, responsabilidad, habilidad_especial)
