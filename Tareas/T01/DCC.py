
import parametros as p
import random
from criaturas import Augurey, Niffler, Erkling
from magizoologos import Docencio, Tareo, Hibrido
from actualizaciones import agregar_magizoologo, agregar_criatura, actualizar_datos_magizoologo
from menus import menu_error, menu_acciones, menu_inicio, menu_cuidar, menu_dcc


class Dcc:

    def __init__(self, magizoologos, criaturas, alimentos, usuario_actual):
        self.magizoologos = magizoologos
        self.criaturas = criaturas
        self.alimentos = alimentos
        self.dias = 1
        self.usuario_actual = usuario_actual

    def crear_magizoologo(self):
        alimentos = []
        criaturas = []
        sickles = p.SICKLES_INICIAL
        licencia = True
        habilidad_especial = True
        while True:
            nombre = input("Ingrese el nombre de su Magizoólogo:")
            if nombre.lower() not in self.magizoologos and nombre.isalnum():
                print(f"Nombre válido. ¡Bienvenido {nombre}!")
                while True:
                    print("¿Qué tipo de Magizoólogo quieres ser?\n[1] "
                          "Docencio\n[2] Tareo\n[3] Híbrido")
                    respuesta = input("Ingrese una opción (1, 2 o 3):")
                    alimentos.append(random.choice(["Tarta de Melaza", "Hígado de Dragón",
                                                    "Buñuelo de Gusarajo"]))
                    condicion = False
                    if respuesta == "1":
                        tipo = "Docencio"
                        nivel_magico = random.randint(p.NIVEL_MAGICO_DOCENCIO_MIN,
                                                      p.NIVEL_MAGICO_DOCENCIO_MAX)
                        destreza = random.randint(p.DESTREZA_DOCENCIO_MIN,
                                                  p.DESTREZA_DOCENCIO_MAX)
                        energia_total = random.randint(p.ENERGIA_TOTAL_DOCENCIO_MIN,
                                                       p.ENERGIA_TOTAL_DOCENCIO_MAX)
                        responsabilidad = random.randint(p.RESPONSABILIDAD_DOCENCIO_MIN,
                                                         p.RESPONSABILIDAD_DOCENCIO_MAX)
                        condicion = self.vender_criatura(criaturas, sickles)
                        if condicion:
                            self.magizoologos[nombre] = Docencio(nombre, tipo, sickles, criaturas,
                                                             alimentos, licencia, nivel_magico,
                                                             destreza, energia_total,
                                                             responsabilidad,
                                                             habilidad_especial)
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
                        condicion = self.vender_criatura(criaturas, sickles)
                        if condicion:
                            self.magizoologos[nombre] = Tareo(nombre, tipo, sickles, criaturas,
                                                          alimentos, licencia, nivel_magico,
                                                          destreza, energia_total,
                                                          responsabilidad,
                                                          habilidad_especial)
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
                        condicion = self.vender_criatura(criaturas, sickles)
                        if condicion:
                            self.magizoologos[nombre] = Hibrido(nombre, tipo, sickles, criaturas,
                                                            alimentos, licencia, nivel_magico,
                                                            destreza, energia_total,
                                                            responsabilidad,
                                                            habilidad_especial)
                    else:
                        print("ERROR. Intenta nuevamente.")
                    if (respuesta == "1" or respuesta == "2" or respuesta == "3") and condicion:
                        print(self.magizoologos[nombre].__dict__)
                        self.usuario_actual = self.magizoologos[nombre]
                        agregar_magizoologo(self.magizoologos[nombre], p.RUTA_MAGIZOOLOGOS)
                        menu_acciones(Dcc(self.magizoologos, self.criaturas, self.alimentos,
                                          self.usuario_actual))
            elif nombre.lower() in self.magizoologos:
                print("Nombre ya existe.\n¿Qué desea hacer?")
                menu_error(Dcc(self.magizoologos, self.criaturas, self.alimentos,
                               self.usuario_actual), menu_inicio)
            else:
                print("Nombre inválido. Solo utilizar caracteres alfanuméricos.\n¿Qué desea hacer?")
                menu_error(Dcc(self.magizoologos, self.criaturas, self.alimentos,
                               self.usuario_actual), menu_inicio)
            if self.usuario_actual is not None:
                break

    def cargar_magizoologo(self):
        while True:
            nombre = input("Ingrese el nombre del Magizoólogo:").lower()
            if nombre.lower() in self.magizoologos and nombre.isalnum():
                self.usuario_actual = self.magizoologos[nombre.lower()]
                print(f"¡Bienvenido {self.usuario_actual.nombre}!")
                menu_acciones(Dcc(self.magizoologos, self.criaturas, self.alimentos,
                                  self.usuario_actual))
            else:
                print("Magizoologo no existe. \n¿Qué desea hacer?")
                menu_error(Dcc(self.magizoologos, self.criaturas, self.alimentos,
                               self.usuario_actual), menu_inicio)

    def vender_criatura(self, criaturas, sickles):
        while True:
            print("¿Qué tipo de DCCriatura quieres?\n[1] Augurey\n"
                  "[2] Niffler\n[3] Erkling")
            respuesta = input("Ingrese una opción (1, 2 o 3):")
            nombre_criatura = None
            estado_salud = False
            nivel_hambre = "satisfecha"
            estado_escape = False
            dias_sin_comer = 0
            if respuesta == "1" and sickles >= p.PRECIO_AUGEREY:
                tipo_criatura = "Augurey"
                nivel_magico_criatura = random.randint(p.NIVEL_MAGICO_AUGUREY_MIN,
                                                       p.NIVEL_MAGICO_AUGUREY_MAX)
                prob_escape = p.PROB_ESCAPE_AUGUREY
                prob_enfermar = p.PROB_ENFERMAR_AUGUREY
                salud_total = p.SALUD_AUGUREY_MAX
                salud_actual = p.SALUD_AUGUREY_MAX
                nivel_agresividad = p.NIVEL_AGRESVIDAD_AUGUREY
                cleptomania = p.CLEPTOMANIA_AUGUREY
                nombre_criatura = self.elegir_nombre_criatura(criaturas)
                if nombre_criatura is not False:
                    self.criaturas[nombre_criatura] = Augurey(nombre_criatura, tipo_criatura,
                                                          nivel_magico_criatura, prob_escape,
                                                          prob_enfermar, estado_salud,
                                                          estado_escape, salud_total, salud_actual,
                                                          nivel_hambre, nivel_agresividad,
                                                          dias_sin_comer, cleptomania)
            elif respuesta == "2" and sickles >= p.PRECIO_NIFFLER:
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
                nombre_criatura = self.elegir_nombre_criatura(criaturas)
                if nombre_criatura is not False:
                    self.criaturas[nombre_criatura] = Niffler(nombre_criatura, tipo_criatura,
                                                          nivel_magico_criatura, prob_escape,
                                                          prob_enfermar, estado_salud,
                                                          estado_escape, salud_total, salud_actual,
                                                          nivel_hambre, nivel_agresividad,
                                                          dias_sin_comer, cleptomania)
            elif respuesta == "3" and sickles >= p.PRECIO_ERKLING:
                tipo_criatura = "Erkling"
                nivel_magico_criatura = random.randint(p.NIVEL_MAGICO_ERKLING_MIN,
                                                       p.NIVEL_MAGICO_ERKLING_MAX)
                prob_escape = p.PROB_ESCAPE_ERKLING
                prob_enfermar = p.PROB_ENFERMAR_ERKLING
                salud_total = p.SALUD_ERKLING_MAX
                salud_actual = p.SALUD_ERKLING_MAX
                nivel_agresividad = p.NIVEL_AGRESVIDAD_ERKLING
                cleptomania = p.CLEPTOMANIA_ERKLING
                nombre_criatura = self.elegir_nombre_criatura(criaturas)

                if nombre_criatura is not False:
                    self.criaturas[nombre_criatura] = Erkling(nombre_criatura, tipo_criatura,
                                                          nivel_magico_criatura, prob_escape,
                                                          prob_enfermar, estado_salud,
                                                          estado_escape, salud_total, salud_actual,
                                                          nivel_hambre, nivel_agresividad,
                                                          dias_sin_comer, cleptomania)
            else:
                print("ERROR. Intente nuevamente")

            if ((respuesta == "1" and sickles >= p.PRECIO_AUGEREY) or (respuesta == "2" and
                sickles >= p.PRECIO_NIFFLER) or (respuesta == "3" and sickles >= p.PRECIO_ERKLING))\
                    and nombre_criatura is not False :
                criaturas.append(nombre_criatura)
                print(self.criaturas[nombre_criatura].__dict__)
                agregar_criatura(self.criaturas[nombre_criatura], p.RUTA_CRIATURAS)
                if len(criaturas) != 1:
                    sickles -= self.criaturas[nombre_criatura].precio
                    return sickles
                return True

    def elegir_nombre_criatura(self, criaturas):
        menu_anterior = menu_inicio
        if len(criaturas) > 0:
            menu_anterior = menu_dcc
        while True:
            nombre_criatura = input("¿Qué nombre quieres ponerle a "
                                    "tu DCC Criatura?")
            if nombre_criatura.lower() not in self.criaturas and nombre_criatura.isalnum():
                print("Nombre válido.")
                return nombre_criatura
            else:
                print("Nombre inválido. ¿Qué desea hacer?")
                menu_error(Dcc(self.magizoologos, self.criaturas, self.alimentos,
                               self.usuario_actual), menu_anterior)

    def mostrar_estado(self):
        user = self.usuario_actual
        print(f"DATOS MAGIZOÓLOGO\nNombre: {user.nombre}\nSickles: {user.sickles}\nEnergía actual: "
              f"{user.energia_actual}\nLicencia: {user.licencia}\nNivel de aprobación: "
              f"{user.nivel_aprobacion}\nNivel mágico: {user.nivel_magico}\nDestreza: "
              f"{user.destreza}\nResponsabilidad: {user.responsabilidad}\n")
        print(f"DATOS ALIMENTOS")
        for alimento in self.alimentos:
            alim = self.alimentos[alimento]
            print(f"Nombre: {alim.nombre}\n  Cantidad: {user.alimentos.count(alim.nombre)}\n  "
                  f"Efecto de Salud: {alim.efecto_salud}\n")
        print("DATOS DCCRIATURAS")
        for criaturas in self.usuario_actual.criaturas:
            criat = self.criaturas[criaturas.lower()]
            print(f"Nombre: {criat.nombre}\n  Tipo: {criat.tipo}\n  Nivel mágico: "
                  f"{criat.nivel_magico}\n  Salud actual: {criat.salud_actual}\n  "
                  f"Estado de salud: {criat.estado_salud}\n  Nivel de hambre: {criat.nivel_hambre}"
                  f"\n  Nivel de agresividad: {criat.nivel_agresividad}\n")




