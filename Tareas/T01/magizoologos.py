
import parametros as p
from actualizaciones import actualizar_datos

class Personajes:

    def __init__(self, nombre, tipo, nivel_magico):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel_magico = nivel_magico

class Magizoologo(Personajes):

    def __init__(self, nombre, tipo, sickles, criaturas, alimentos, licencia, nivel_magico,
                 destreza, energia, responsabilidad, habilidad_especial):
        super().__init__(nombre, tipo, nivel_magico)
        self.sickles = int(sickles)
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
            print(f"Los precios son los siguientes:\nAugurey: {p.PRECIO_AUGEREY}\nNiffler: "
                  f"{p.PRECIO_NIFFLER}\nErkling: {p.PRECIO_ERKLING}")
            print(f"Tu saldo actual es de {self.sickles} Sickles")
            self.sickles = DCC.vender_criatura(self.criaturas, self.sickles)
            print("¡DCCriatura adoptada con éxito!")
            print(f"Tu saldo actual es de {self.sickles} Sickles")
            actualizar_datos(DCC.usuario_actual, p.RUTA_MAGIZOOLOGOS)

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
