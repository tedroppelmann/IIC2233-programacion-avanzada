
import parametros as p
from actualizaciones import actualizar_datos_magizoologo, actualizar_datos_criaturas
from menus import menu_error, menu_dcc, menu_cuidar
from abc import ABC, abstractmethod
import random


class Magizoologo(ABC):

    def __init__(self, nombre, tipo, sickles, criaturas, alimentos, licencia, nivel_magico,
                 destreza, energia, responsabilidad, habilidad_especial):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel_magico = int(nivel_magico)
        self.sickles = int(sickles)
        self.criaturas = criaturas
        self.alimentos = alimentos
        self.licencia = licencia
        self.destreza = int(destreza)
        self.energia = int(energia)
        self.responsabilidad = responsabilidad
        self.habilidad_especial = habilidad_especial

        self.energia_actual = int(energia)
        self.nivel_aprobacion = None

    def adoptar(self, DCC):
        if self.licencia:
            print(f"Los precios son los siguientes:\nAugurey: {p.PRECIO_AUGEREY}\nNiffler: "
                  f"{p.PRECIO_NIFFLER}\nErkling: {p.PRECIO_ERKLING}")
            print(f"Tu saldo actual es de {self.sickles} Sickles")
            self.sickles = DCC.vender_criatura(self.criaturas, self.sickles)
            print("¡DCCriatura adoptada con éxito!")
            print(f"Tu saldo actual es de {self.sickles} Sickles")
            actualizar_datos_magizoologo(DCC.usuario_actual, p.RUTA_MAGIZOOLOGOS)
        else:
            print("No posees licencia, por lo que no puedes adpotar una DCCriatura.")

    def comprar_alimento(self, DCC):
        print(f"Los precios son los siguientes:")
        i = 1
        for nombre in DCC.alimentos.keys():
            print(f"[{i}] {DCC.alimentos[nombre].nombre}: {DCC.alimentos[nombre].precio} Sickles")
            i += 1
        print(f"Actualmente posees {self.sickles} Sickles")
        while True:
            respuesta = input("Ingrese una opción (1, 2 o 3):")
            if respuesta == "1":
                precio = p.PRECIO_TARTA_MELAZA
                if sickles_suficiente(self.sickles, precio):
                    compra = "Tarta de Melaza"
                    break
                else:
                    print("No tienes dinero suficiente. ¿Qué deseas hacer?")
                    menu_error(DCC, menu_dcc)
            elif respuesta == "2":
                precio = p.PRECIO_HIGADO_DRAGON
                if sickles_suficiente(self.sickles, precio):
                    compra = "Hígado de Dragón"
                    break
                else:
                    print("No tienes dinero suficiente. ¿Qué deseas hacer?")
                    menu_error(DCC, menu_dcc)
            elif respuesta == "3":
                precio = p.PRECIO_BUNUELOS_GUSARAJO
                if sickles_suficiente(self.sickles, precio):
                    compra = "Buñuelos de Gusarajo"
                    break
                else:
                    print("No tienes dinero suficiente. ¿Qué deseas hacer?")
                    menu_error(DCC, menu_dcc)
            else:
                print("ERROR. Intente nuevamente.")
        self.alimentos.append(compra)
        self.sickles -= precio
        actualizar_datos_magizoologo(DCC.usuario_actual, p.RUTA_MAGIZOOLOGOS)
        print(f"¡Compraste {compra}!")
        print(f"Tu saldo actual es de {self.sickles} Sickles")

    @abstractmethod
    def alimentar_criatura(self, DCC):
        if len(self.alimentos) >= 1 and self.alimentos[0] != "":
            if self.energia_actual >= p.GASTO_ALIMENTAR:
                while True:
                    print(f"¿A cuál de tus DCCriaturas quieres alimentar?")
                    i = 0
                    for criaturas in self.criaturas:
                        criat = DCC.criaturas[criaturas.lower()]
                        if not criat.estado_escape:
                            print(f"[{i+1}] {criat.nombre} ({criat.tipo}): {criat.nivel_hambre}")
                            i += 1
                        elif i == 0:
                            print("Hay un problema. Todas tus criaturas han escapado. "
                                  "¡Ve a recuperarlas!")
                            return criat, False
                    nombre = input("Escribe su nombre:")
                    while True:
                        print("Posees los siguientes alimentos:")
                        for alimento in DCC.alimentos:
                            alim = DCC.alimentos[alimento]
                            if alim.nombre in self.alimentos:
                                print(f"{alim.nombre}\n  Cantidad: "
                                      f"{self.alimentos.count(alim.nombre)}")
                        resp = input("¿Que alimento quieres utilizar? "
                                     "Escribe su nombre (con tildes):")
                        j = 0
                        alimento_elegido = None
                        for alimento in DCC.alimentos:
                            alim = DCC.alimentos[alimento]
                            if resp.lower() == alim.nombre.lower() and resp.lower() in \
                                    (element.lower() for element in self.alimentos):
                                alimento_elegido = alim
                                j += 1
                        if j == 1:
                            break
                        else:
                            print("Nombre incorrecto. ¿Qué deseas hacer?")
                            menu_error(DCC, menu_cuidar)
                    for criaturas in self.criaturas:
                        criat = DCC.criaturas[criaturas.lower()]
                        if nombre.lower() == criat.nombre.lower() and not criat.estado_escape and \
                                alimento_elegido:
                            self.energia_actual -= int(criat.alimentarse(DCC))
                            criat.salud_actual += alimento_elegido.efecto_salud
                            self.alimentos.remove(alimento_elegido.nombre)
                            self.energia_actual -= p.GASTO_ALIMENTAR
                            alimento_elegido.particularidad_alimento(DCC, criat)
                            if criat.nivel_hambre == "satisfecha":
                                criat.dias_sin_comer = 0
                                actualizar_datos_criaturas(criat, p.RUTA_CRIATURAS)
                                actualizar_datos_magizoologo(DCC.usuario_actual,
                                                             p.RUTA_MAGIZOOLOGOS)
                                print(f"Tu energía actual es de {self.energia_actual}")
                                return criat, True
                            else:
                                actualizar_datos_criaturas(criat, p.RUTA_CRIATURAS)
                                actualizar_datos_magizoologo(DCC.usuario_actual,p.RUTA_MAGIZOOLOGOS)
                                print(f"Tu energía actual es de {self.energia_actual}")
                                return criat, False
                    print("Nombre incorrecto. ¿Qué deseas hacer?")
                    menu_error(DCC, menu_cuidar)
            else:
                print("No posees la suficiente energía actualmente para alimentar una DCCriatura.")
        else:
            print("No posees alimentos actualmente.")
            return None, False

    @abstractmethod
    def recuperar_criatura(self, DCC):
        if self.energia_actual >= p.GASTO_RECUPERAR:
            while True:
                i = 0
                print("Las DCCriaturas que han escapado son:")
                for criaturas in self.criaturas:
                    criat = DCC.criaturas[criaturas.lower()]
                    if criat.estado_escape:
                        print(f"[{i+1}] {criat.nombre} ({criat.tipo}):"
                              f"\n  Nivel mágico: {criat.nivel_magico}")
                        i += 1
                    elif i == 0:
                        print("¡Felicitaciones! No se ha escapado ninguna DCCriatura")
                        return None, False
                nombre = input("Escribe el nombre de la DCCriatura que quieres rescatar:")
                for criaturas in self.criaturas:
                    criat = DCC.criaturas[criaturas.lower()]
                    if nombre.lower() == criat.nombre.lower() and criat.estado_escape:
                        self.energia_actual -= p.GASTO_RECUPERAR
                        prob_exito = min(1, max(0,(self.destreza + self.nivel_magico
                                                   - criat.nivel_magico)/
                                                (self.destreza + self.nivel_magico +
                                                 criat.nivel_magico)))
                        if random.random() <= prob_exito:
                            criat.estado_escape = False
                            actualizar_datos_criaturas(criat, p.RUTA_CRIATURAS)
                            print(f"Has recuperado a {criat.nombre} ¡Felicitiaciones!")
                            print(f"Tu energía actual es de {self.energia_actual}")
                            return criat, True
                        else:
                            actualizar_datos_criaturas(criat, p.RUTA_CRIATURAS)
                            print(f"No lograste recuperar a {criat.nombre}.")
                            print(f"Tu energía actual es de {self.energia_actual}")
                            menu_cuidar(DCC)
                print("Nombre incorrecto. ¿Qué deseas hacer?")
                menu_error(DCC, menu_cuidar)
        else:
            print("No posees la sufiente energía actualmente para recuperar una DCCriatura.")
            return None, False

    def usar_habilidad_especial(self, DCC):
        pass

class Docencio(Magizoologo):

    def alimentar_criatura(self, DCC):
        criatura, condicion = super().alimentar_criatura(DCC)
        if condicion:
            criatura.salud_total += p.DOCENCIO_AUMENTO_SALUD_TOTAL_CRIATURA
            print(f"Como eres Docencio, {criatura.nombre} ahora posee "
                  f"{criatura.salud_total} puntos de salud total.")
            actualizar_datos_criaturas(criatura, p.RUTA_CRIATURAS)

    def recuperar_criatura(self, DCC):
        criatura, condicion = super().recuperar_criatura(DCC)
        if condicion:
            criatura.salud_actual -= p.DOCENCIO_COSTO_RECUPERAR_CRIATURA
            print(f"Como eres Docencio, {criatura.nombre} ahora posee "
                  f"{criatura.salud_actual} puntos de salud total, debido a problemas "
                  f"al capturarla.")
            actualizar_datos_criaturas(criatura, p.RUTA_CRIATURAS)

    def usar_habilidad_especial(self, DCC):
        if self.energia_actual >= p.COSTO_HABILIDAD_ESPECIAL:
            if self.habilidad_especial:
                for criaturas in self.criaturas:
                    criatura = DCC.criaturas[criaturas.lower()]
                    criatura.nivel_hambre = "satisfecha"
                    criaturas.dias_sin_comer = 0
                    actualizar_datos_criaturas(criatura, p.RUTA_CRIATURAS)
                print("Has tu utilizado tu habilidad especial de Docencio. ¡Ahora todas "
                      "tus criaturas están satisfechas!")
                self.habilidad_especial = False
                actualizar_datos_magizoologo(DCC.usuario_actual, p.RUTA_MAGIZOOLOGOS)
            else:
                print("Ya has utilizado tu habilidad especial. No puedes volver a usarla. ")
        else:
            print("No tienes la suficiente energía actualmente para utilizar tu "
                  "habilidad especial.")

class Tareo(Magizoologo):

    def alimentar_criatura(self,DCC):
        criatura, condicion = super().alimentar_criatura(DCC)
        if condicion:
            if random.random() < p.PROB_SALUD_TAREO:
                criatura.salud_actual = criatura.salud_total
                print(f"¡Enhorabuena! Como eres Tareo, {criatura.nombre} ahora posee "
                      f"{criatura.salud_total} puntos de salud actual, el total de sus "
                      f"puntos de salud.")
                actualizar_datos_criaturas(criatura, p.RUTA_CRIATURAS)

    def recuperar_criatura(self, DCC):
        criatura, condicion = super().recuperar_criatura(DCC)
        if condicion:
            print(f"¡Enhorabuena! Como eres Tareo, {criatura.nombre} "
                  f"no se ve afectada al capturarla.")

    def usar_habilidad_especial(self, DCC):
        if self.energia_actual >= p.COSTO_HABILIDAD_ESPECIAL:
            if self.habilidad_especial:
                for criaturas in self.criaturas:
                    criatura = DCC.criaturas[criaturas.lower()]
                    criatura.estado_escape = False
                    actualizar_datos_criaturas(criatura, p.RUTA_CRIATURAS)
                print("Has tu utilizado tu habilidad especial de Tareo. ¡Ahora todas tus criaturas"
                      " han sido capturadas!")
                self.habilidad_especial = False
                self.energia_actual -= p.COSTO_HABILIDAD_ESPECIAL
                actualizar_datos_magizoologo(DCC.usuario_actual, p.RUTA_MAGIZOOLOGOS)
            else:
                print("Ya has utilizado tu habilidad especial. No puedes volver a usarla. ")
        else:
            print("No tienes la suficiente energía actualmente para utilizar tu "
                  "habilidad especial.")

class Hibrido(Magizoologo):

    def alimentar_criatura(self,DCC):
        criatura, condicion = super().alimentar_criatura(DCC)
        if condicion:
            criatura.salud_total += p.HIBRIDO_AUMENTO_SALUD_ACTUAL_CRIATURA
            print(f"¡Enhorabuena! Como eres Híbrido, {criatura.nombre} ahora posee "
                  f"{criatura.salud_total} puntos de salud actual.")
            actualizar_datos_criaturas(criatura, p.RUTA_CRIATURAS)

    def recuperar_criatura(self, DCC):
        criatura, condicion = super().recuperar_criatura(DCC)
        if condicion:
            print(f"¡Enhorabuena! Como eres Híbrido, {criatura.nombre} "
                  f"no se ve afectada al capturarla.")

    def usar_habilidad_especial(self, DCC):
        if self.energia_actual >= p.COSTO_HABILIDAD_ESPECIAL:
            if self.habilidad_especial:
                for criaturas in self.criaturas:
                    criatura = DCC.criaturas[criaturas.lower()]
                    criatura.estado_salud = False
                    actualizar_datos_criaturas(criatura, p.RUTA_CRIATURAS)
                print("Has tu utilizado tu habilidad especial de Híbrido. ¡Ahora todas tus "
                      "criaturas están sanas!")
                self.habilidad_especial = False
                actualizar_datos_magizoologo(DCC.usuario_actual, p.RUTA_MAGIZOOLOGOS)
            else:
                print("Ya has utilizado tu habilidad especial. No puedes volver a usarla. ")
        else:
            print("No tienes la suficiente energía actualmente para utilizar tu habilidad "
                  "especial.")

def sickles_suficiente(sickles, precio):
    if sickles >= precio:
        sickles -= precio
        return True, sickles
    else:
        return False