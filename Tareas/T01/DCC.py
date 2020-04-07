
import sys
import parametros as p
import random
from criaturas import Augurey, Niffler, Erkling
from magizoologos import Docencio, Tareo, Hibrido
from actualizaciones import agregar_magizoologo, agregar_criatura

class Dcc:

    def __init__(self, magizoologos, criaturas, alimentos):
        self.magizoologos = magizoologos
        self.criaturas = criaturas
        self.alimentos = alimentos
        self.usuario_actual = None
        self.magizoologos_minusculas = []
        self.criaturas_minusculas = []
        for user in self.magizoologos:
            self.magizoologos_minusculas.append(user.lower())
        for user in self.criaturas:
            self.criaturas_minusculas.append(user.lower())

    def crear_magizoologo(self):
        alimentos = []
        criaturas = []
        tipo = None
        nivel_magico = None
        destreza = None
        sickles = p.SICKLES_INICIAL
        licencia = True
        habilidad_especial = True
        responsabilidad = None
        energia_total = None
        nombre_criatura = None
        while True:
            nombre = input("Ingrese el nombre de su Magizoólogo:")
            if nombre.lower() not in self.magizoologos_minusculas and nombre.isalnum():
                print(f"Nombre válido. ¡Bienvenido {nombre}! ")
                while True:
                    print("¿Qué tipo de Magizoólogo quieres ser?\n[1] "
                          "Docencio\n[2] Tareo\n[3] Híbrido")
                    respuesta = input("Ingrese una opción (1, 2 o 3):")
                    i = 0
                    if respuesta == "1":
                        tipo = "Docecio"
                        nivel_magico = random.randint(p.NIVEL_MAGICO_DOCENCIO_MIN,
                                                      p.NIVEL_MAGICO_DOCENCIO_MAX)
                        destreza = random.randint(p.DESTREZA_DOCENCIO_MIN,
                                                  p.DESTREZA_DOCENCIO_MAX)
                        energia_total = random.randint(p.ENERGIA_TOTAL_DOCENCIO_MIN,
                                                       p.ENERGIA_TOTAL_DOCENCIO_MAX)
                        responsabilidad = random.randint(p.RESPONSABILIDAD_DOCENCIO_MIN,
                                                         p.RESPONSABILIDAD_DOCENCIO_MAX)
                        i +=1
                    elif respuesta == "2":
                        tipo = "Tareo"
                        nivel_magico = random.randint(p.NIVEL_MAGICO_TAREO_MIN,
                                                      p.NIVEL_MAGICO_TAREO_MAX)
                        destreza = random.randint(p.DESTREZA_TAREO_MIN,
                                                  p.DESTREZA_TAREO_MAX)
                        energia_total = random.randint(p.ENERGIA_TOTAL_TAREO_MIN,
                                                       p.ENERGIA_TOTAL_TAREO_MAX)
                        responsabilidad = random.randint(p.RESPONSABILIDAD_DOCENCIO_MIN,
                                                         p.RESPONSABILIDAD_TAREO_MAX)
                        i +=1
                    elif respuesta == "3":
                        tipo = "Híbrido"
                        nivel_magico = random.randint(p.NIVEL_MAGICO_HIBRIDO_MIN,
                                                      p.NIVEL_MAGICO_HIBRIDO_MAX)
                        destreza = random.randint(p.DESTREZA_HIBRIDO_MIN,
                                                  p.DESTREZA_HIBRIDO_MAX)
                        energia_total = random.randint(p.ENERGIA_TOTAL_HIBRIDO_MIN,
                                                       p.ENERGIA_TOTAL_HIBRIDO_MAX)
                        responsabilidad = random.randint(p.RESPONSABILIDAD_HIBRIDO_MIN,
                                                         p.RESPONSABILIDAD_HIBRIDO_MAX)
                        i += 1
                    else:
                        print("ERROR. Intenta nuevamente.")
                    if i == 1:
                        alimentos.append(random.choice(["Tarta de Melaza", "Hígado de Dragón",
                                                        "Buñuelo de Guasarajo"]))
                        while True:
                            nombre_criatura = input("¿Qué nombre quieres ponerle a "
                                                    "tu DCC Criatura?")
                            if nombre_criatura.lower() not in self.criaturas_minusculas \
                                    and nombre_criatura.isalnum():
                                print("Nombre válido.")
                                i += 1
                                break
                            else:
                                print("Nombre inválido. Intenta nuevamente.")
                    if i ==2:
                        while True:
                            print("¿Qué tipo de DCCriatura quieres?\n[1] Augurey\n"
                                  "[2] Niffler\n[3] Erkling")
                            respuesta = input("Ingrese una opción (1, 2 o 3):")
                            criaturas.append(nombre_criatura)
                            estado_salud = True
                            nivel_hambre = "satisfecha"
                            estado_escape = False
                            dias_sin_comer = 0
                            if respuesta == "1":
                                tipo_criatura = "Augurey"
                                nivel_magico_criatura = random.randint(p.NIVEL_MAGICO_AUGUREY_MIN,
                                                                       p.NIVEL_MAGICO_AUGUREY_MAX)
                                prob_escape = p.PROB_ESCAPE_AUGUREY
                                prob_enfermar = p.PROB_ENFERMAR_AUGUREY
                                salud_total = p.SALUD_AUGUREY_MAX
                                salud_actual = p.SALUD_AUGUREY_MAX
                                nivel_agresividad = p.NIVEL_AGRESVIDAD_AUGUREY
                                cleptomania = p.CLEPTOMANIA_AUGUREY
                                self.criaturas[nombre_criatura] = Augurey(nombre_criatura,
                                                                            tipo_criatura,
                                                                            nivel_magico_criatura,
                                                                            prob_escape,
                                                                            prob_enfermar,
                                                                            estado_salud,
                                                                            estado_escape,
                                                                            salud_total,
                                                                            salud_actual,
                                                                            nivel_hambre,
                                                                            nivel_agresividad,
                                                                          dias_sin_comer,
                                                                          cleptomania)
                                i += 1
                                break
                            elif respuesta == "2":
                                tipo_criatura = "Niffler"
                                nivel_magico_criatura = random.randint(p.NIVEL_MAGICO_NIFFLER_MIN,
                                                                       p.NIVEL_MAGICO_NIFFLER_MAX)
                                prob_escape = p.PROB_ESCAPE_NIFFLER
                                prob_enfermar = p.PROB_ENFERMAR_NIFFLER
                                salud_total = p.SALUD_NIFFLER_MAX
                                salud_actual = p.SALUD_NIFFLER_MAX
                                nivel_agresividad = p.NIVEL_AGRESVIDAD_NIFFLER
                                cleptomania = random.randint(p.CLEPTOMANIA_NIFFLER_MIN,
                                                             p.CLEPTOMANIA_NIFFLER_MAX)
                                self.criaturas[nombre_criatura] = Niffler(nombre_criatura,
                                                                          tipo_criatura,
                                                                          nivel_magico_criatura,
                                                                          prob_escape,
                                                                          prob_enfermar,
                                                                          estado_salud,
                                                                          estado_escape,
                                                                          salud_total,
                                                                          salud_actual,
                                                                          nivel_hambre,
                                                                          nivel_agresividad,
                                                                          dias_sin_comer,
                                                                          cleptomania)
                                i += 1
                                break
                            elif respuesta == "3":
                                tipo_criatura = "Erkling"
                                nivel_magico_criatura = random.randint(p.NIVEL_MAGICO_ERKLING_MIN,
                                                                       p.NIVEL_MAGICO_ERKLING_MAX)
                                prob_escape = p.PROB_ESCAPE_ERKLING
                                prob_enfermar = p.PROB_ENFERMAR_ERKLING
                                salud_total = p.SALUD_ERKLING_MAX
                                salud_actual = p.SALUD_ERKLING_MAX
                                nivel_agresividad = p.NIVEL_AGRESVIDAD_ERKLING
                                cleptomania = p.CLEPTOMANIA_ERKLING
                                self.criaturas[nombre_criatura] = Erkling(nombre_criatura,
                                                                          tipo_criatura,
                                                                          nivel_magico_criatura,
                                                                          prob_escape,
                                                                          prob_enfermar,
                                                                          estado_salud,
                                                                          estado_escape,
                                                                          salud_total,
                                                                          salud_actual,
                                                                          nivel_hambre,
                                                                          nivel_agresividad,
                                                                          dias_sin_comer,
                                                                          cleptomania)
                                i += 1
                                break
                            else:
                                print("ERROR. Intenta nuevamente.")
                    if i == 3:
                        if tipo == "Docecio":
                            self.magizoologos[nombre] = Docencio(nombre, tipo, sickles, criaturas,
                                                                alimentos, licencia, nivel_magico,
                                                                destreza, energia_total,
                                                                responsabilidad,
                                                                habilidad_especial)
                        elif tipo == "Tareo":
                            self.magizoologos[nombre] = Tareo(nombre, tipo, sickles, criaturas,
                                                                alimentos, licencia, nivel_magico,
                                                                destreza, energia_total,
                                                                responsabilidad,
                                                                habilidad_especial)
                        elif tipo == "Híbrido":
                            self.magizoologos[nombre] = Hibrido(nombre, tipo, sickles, criaturas,
                                                                alimentos, licencia, nivel_magico,
                                                                destreza, energia_total,
                                                                responsabilidad,
                                                                habilidad_especial)
                    break
            elif nombre.lower() in self.magizoologos_minusculas:
                print("Nombre ya existe.\n¿Qué desea hacer?")
                return error()
            else:
                print("Nombre inválido. Solo utilizar carcteres alfanuméricos.\n¿Qué desea hacer?")
                return error()
            self.usuario_actual = self.magizoologos[nombre]
            print(self.magizoologos[nombre].__dict__)
            print(self.criaturas[nombre_criatura].__dict__)
            agregar_magizoologo(self.usuario_actual, "magizoologos.csv")
            agregar_criatura(self.criaturas[nombre_criatura], "criaturas.csv")
            break

    def cargar_magizoologo(self):

        while True:
            nombre = input("Ingrese el nombre del Magizoólogo:").lower()
            for user in self.magizoologos:
                if nombre == user.lower():
                    print(f"¡Bienvenido {nombre}!")
                    self.usuario_actual = self.magizoologos[nombre]
                    return False

            print("Magizoologo no existe. \n¿Qué desea hacer?")
            return error()

    def vender_criatura(self, criatura):
        pass

class Alimento:

    def __init__(self, nombre, efecto_salud, precio):
        self.nombre = nombre
        self.efecto_salud = efecto_salud
        self.precio = precio


def error():
    print("[1] Intentar de nuevo \n[2] Volver atrás \n[0] Salir")
    respuesta = input("Ingrese una opción (1, 2 o 0):")
    if respuesta == "1":
        pass
    elif respuesta == "2":
        return False
    elif respuesta == "0":
        sys.exit()