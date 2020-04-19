
import parametros as p
import random
from criaturas import Augurey, Niffler, Erkling
from magizoologos import Docencio, Tareo, Hibrido
from actualizaciones import agregar_magizoologo, agregar_criatura, actualizar_datos_magizoologo, \
    actualizar_datos_criaturas
from menus import menu_error, menu_acciones, menu_inicio, menu_dcc

class Dcc:

    def __init__(self, magizoologos, criaturas, alimentos, usuario_actual):
        self.magizoologos = magizoologos
        self.criaturas = criaturas
        self.alimentos = alimentos
        self.usuario_actual = usuario_actual

    def crear_magizoologo(self):
        """
        Permite crear un nuevo magizoologo
        :return: None
        """
        alimentos = []
        criaturas = []
        sickles = p.SICKLES_INICIAL
        licencia = True
        habilidad_especial = True
        alimentos.append(random.choice(["Tarta de Melaza", "Hígado de Dragón",
                                        "Buñuelo de Gusarajo"]))
        while True:
            nombre = input("Ingrese el nombre de su Magizoólogo:")
            if nombre.lower() not in self.magizoologos and nombre.isalnum():
                print(f"Nombre válido. ¡Bienvenido {nombre}!")
                while True:
                    print("¿Qué tipo de Magizoólogo quieres ser?\n[1] "
                          "Docencio\n[2] Tareo\n[3] Híbrido")
                    respuesta = input("Ingrese una opción (1, 2 o 3):")
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
                            self.magizoologos[nombre.lower()] = Docencio(nombre, tipo, sickles,
                                                                         criaturas, alimentos,
                                                                         licencia, nivel_magico,
                                                                         destreza, energia_total,
                                                                         responsabilidad,
                                                                         habilidad_especial)
                            print(self.magizoologos[nombre.lower()])
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
                            self.magizoologos[nombre.lower()] = Tareo(nombre, tipo, sickles,
                                                                         criaturas, alimentos,
                                                                         licencia, nivel_magico,
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
                            self.magizoologos[nombre.lower()] = Hibrido(nombre, tipo, sickles,
                                                                         criaturas, alimentos,
                                                                         licencia, nivel_magico,
                                                                         destreza, energia_total,
                                                                         responsabilidad,
                                                                         habilidad_especial)
                    else:
                        print("ERROR. Intenta nuevamente.")
                    if (respuesta == "1" or respuesta == "2" or respuesta == "3") and condicion:
                        self.usuario_actual = self.magizoologos[nombre.lower()]
                        self.usuario_actual.nivel_aprobacion = p.APROBACION_MAXIMA
                        agregar_magizoologo(self.usuario_actual, p.RUTA_MAGIZOOLOGOS)
                        menu_acciones(self)
            elif nombre.lower() in self.magizoologos:
                print("Nombre ya existe.\n¿Qué desea hacer?")
                menu_error(self, menu_inicio)
            else:
                print("Nombre inválido. Solo utilizar caracteres alfanuméricos.\n¿Qué desea hacer?")
                menu_error(self, menu_inicio)
            if self.usuario_actual is not None:
                break

    def cargar_magizoologo(self):
        """
        Permite cargar un magizoolo desde la población que se cargo del archivo .csv
        :return: None
        """
        while True:
            nombre = input("Ingrese el nombre del Magizoólogo:").lower()
            if nombre.lower() in self.magizoologos and nombre.isalnum():
                self.usuario_actual = self.magizoologos[nombre.lower()]
                print(f"¡Bienvenido {self.usuario_actual.nombre}!")
                menu_acciones(self)
            else:
                print("Magizoologo no existe. \n¿Qué desea hacer?")
                menu_error(self, menu_inicio)

    def vender_criatura(self, criaturas, sickles):
        """
        Permite adquirir una nueva criatura
        :param criaturas: list
        :param sickles: int
        :return: bool
        """
        while True:
            print("¿Qué tipo de DCCriatura quieres?\n[1] Augurey\n"
                  "[2] Niffler\n[3] Erkling")
            respuesta = input("Ingrese una opción (1, 2 o 3):")
            nombre_criatura = None
            estado_salud = False
            nivel_hambre = "satisfecha"
            estado_escape = False
            dias_sin_comer = 0
            if respuesta == "1":
                if sickles >= p.PRECIO_AUGEREY:
                    tipo_criatura = "Augurey"
                    nivel_magico_criatura = random.randint(p.NIVEL_MAGICO_AUGUREY_MIN,
                                                           p.NIVEL_MAGICO_AUGUREY_MAX)
                    prob_escape = p.PROB_ESCAPE_AUGUREY
                    prob_enfermar = p.PROB_ENFERMAR_AUGUREY
                    salud_total = random.randint(p.SALUD_AUGUREY_MIN, p.SALUD_AUGUREY_MAX)
                    salud_actual = salud_total
                    nivel_agresividad = p.NIVEL_AGRESVIDAD_AUGUREY
                    cleptomania = p.CLEPTOMANIA_AUGUREY
                    nombre_criatura = self.elegir_nombre_criatura(criaturas)
                    if nombre_criatura is not False:
                        self.criaturas[nombre_criatura.lower()] = Augurey(nombre_criatura,
                                                                          tipo_criatura,
                                                                          nivel_magico_criatura,
                                                                          prob_escape,
                                                                          prob_enfermar,
                                                                          estado_salud,
                                                                          estado_escape,
                                                                          salud_total, salud_actual,
                                                                          nivel_hambre,
                                                                          nivel_agresividad,
                                                                          dias_sin_comer,
                                                                          cleptomania)
                elif sickles < p.PRECIO_AUGEREY:
                    print("No tienes dinero suficiente.")
                    menu_dcc(self)
            elif respuesta == "2":
                if sickles >= p.PRECIO_NIFFLER:
                    tipo_criatura = "Niffler"
                    nivel_magico_criatura = random.randint(p.NIVEL_MAGICO_NIFFLER_MIN,
                                                           p.NIVEL_MAGICO_NIFFLER_MAX)
                    prob_escape = p.PROB_ESCAPE_NIFFLER
                    prob_enfermar = p.PROB_ENFERMAR_NIFFLER
                    salud_total = random.randint(p.SALUD_NIFFLER_MIN, p.SALUD_NIFFLER_MAX)
                    salud_actual = salud_total
                    nivel_agresividad = p.NIVEL_AGRESVIDAD_NIFFLER
                    cleptomania = random.randint(p.CLEPTOMANIA_NIFFLER_MIN,
                                                 p.CLEPTOMANIA_NIFFLER_MAX)
                    nombre_criatura = self.elegir_nombre_criatura(criaturas)
                    if nombre_criatura is not False:
                        self.criaturas[nombre_criatura.lower()] = Niffler(nombre_criatura,
                                                                          tipo_criatura,
                                                                          nivel_magico_criatura,
                                                                          prob_escape,
                                                                          prob_enfermar,
                                                                          estado_salud,
                                                                          estado_escape,
                                                                          salud_total, salud_actual,
                                                                          nivel_hambre,
                                                                          nivel_agresividad,
                                                                          dias_sin_comer,
                                                                          cleptomania)
                elif sickles < p.PRECIO_NIFFLER:
                    print("No tienes dinero suficiente.")
                    menu_dcc(self)
            elif respuesta == "3":
                if sickles >= p.PRECIO_ERKLING:
                    tipo_criatura = "Erkling"
                    nivel_magico_criatura = random.randint(p.NIVEL_MAGICO_ERKLING_MIN,
                                                           p.NIVEL_MAGICO_ERKLING_MAX)
                    prob_escape = p.PROB_ESCAPE_ERKLING
                    prob_enfermar = p.PROB_ENFERMAR_ERKLING
                    salud_total = random.randint(p.SALUD_ERKLING_MIN, p.SALUD_ERKLING_MAX)
                    salud_actual = salud_total
                    nivel_agresividad = p.NIVEL_AGRESVIDAD_ERKLING
                    cleptomania = p.CLEPTOMANIA_ERKLING
                    nombre_criatura = self.elegir_nombre_criatura(criaturas)
                    if nombre_criatura is not False:
                        self.criaturas[nombre_criatura.lower()] = Erkling(nombre_criatura,
                                                                          tipo_criatura,
                                                                          nivel_magico_criatura,
                                                                          prob_escape,
                                                                          prob_enfermar,
                                                                          estado_salud,
                                                                          estado_escape,
                                                                          salud_total, salud_actual,
                                                                          nivel_hambre,
                                                                          nivel_agresividad,
                                                                          dias_sin_comer,
                                                                          cleptomania)
                elif sickles < p.PRECIO_ERKLING:
                    print("No tienes dinero suficiente.")
                    menu_dcc(self)
            else:
                print("ERROR. Intente nuevamente")

            if ((respuesta == "1" and sickles >= p.PRECIO_AUGEREY) or (respuesta == "2" and
                sickles >= p.PRECIO_NIFFLER) or (respuesta == "3" and sickles >= p.PRECIO_ERKLING))\
                    and nombre_criatura is not False :
                criaturas.append(nombre_criatura)
                agregar_criatura(self.criaturas[nombre_criatura.lower()], p.RUTA_CRIATURAS)
                if len(criaturas) != 1:
                    sickles -= self.criaturas[nombre_criatura.lower()].precio
                    return sickles
                return True

    def elegir_nombre_criatura(self, criaturas):
        """
        Permite elegir un nombre válido para una nueva criatura
        :param criaturas: list
        :return: str
        """
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
                menu_error(self, menu_anterior)

    def mostrar_estado(self):
        """
        Muestra el estado del magizoologo y sus criaturas
        :return: None
        """
        user = self.usuario_actual
        print(f"DATOS MAGIZOÓLOGO\nNombre: {user.nombre}\n  Tipo: {user.tipo}\n  Sickles: "
              f"{user.sickles}\n  Energía actual: "
              f"{user.energia_actual}\n  Licencia: {user.licencia}\n  Nivel de aprobación: "
              f"{user.nivel_aprobacion}\n  Nivel mágico: {user.nivel_magico}\n  Destreza: "
              f"{user.destreza}\n  Responsabilidad: {user.responsabilidad}\n")
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
                  f"Salud total: {criat.salud_total}\n  "
                  f"Estado de salud: {criat.estado_salud}\n  Nivel de hambre: {criat.nivel_hambre}"
                  f"\n  Nivel de agresividad: {criat.nivel_agresividad}\n  "
                  f"Días sin comer: {criat.dias_sin_comer}")

    def calcular_aprobacion(self):
        """
        Calcula la aprobación del magizoologo
        :return: None
        """
        criaturas_sanas = 0
        criaturas_retenidas = 0
        criaturas_totales = 0
        for nombre_criatura in self.usuario_actual.criaturas:
            if not self.criaturas[nombre_criatura.lower()].estado_salud:
                criaturas_sanas += 1
            if not self.criaturas[nombre_criatura.lower()].estado_escape:
                criaturas_retenidas += 1
            criaturas_totales += 1
        aprobacion = min(100, max(0, ((criaturas_sanas + criaturas_retenidas)/
                                      (2 * criaturas_totales)) * 100))
        self.usuario_actual.nivel_aprobacion = int(aprobacion)
        print(f"Nivel de aprobación: {self.usuario_actual.nivel_aprobacion}")
        if self.usuario_actual.nivel_aprobacion >= p.NIVEL_APROBACION_LICENCIA and \
                self.usuario_actual.licencia:
            print(f"¡Felicidades! Continúas con tu licencia")
            self.usuario_actual.licencia = True
        elif self.usuario_actual.nivel_aprobacion >= p.NIVEL_APROBACION_LICENCIA and not \
                self.usuario_actual.licencia:
            self.usuario_actual.licencia = True
            print(f"¡Felicidades! Has recuperado tu licencia")
        elif self.usuario_actual.nivel_aprobacion < p.NIVEL_APROBACION_LICENCIA and not \
                self.usuario_actual.licencia:
            print(f"Lamentablemente aún no logras recuperar tu licencia")
            self.usuario_actual.licencia = False
        else:
            self.usuario_actual.licencia = False
            print(f"Lamentablemente pierdes tu licencia")
        actualizar_datos_magizoologo(self.usuario_actual, p.RUTA_MAGIZOOLOGOS)

    def pagar(self):
        """
        Permite el pago desde el DCC al magizoologo
        :return: None
        """
        pago = self.usuario_actual.nivel_aprobacion * 4 + \
               len(self.usuario_actual.alimentos) * 15 + self.usuario_actual.nivel_magico * 3
        self.usuario_actual.sickles += int(pago)
        print(f"El DCC te ha pagado {int(pago)} Sickles")

    def fiscalizar(self, enfermos_nuevos, escapadores_nuevos):
        """
        Acumula las multas que se deben dar al magizoologo
        :param enfermos_nuevos: list
        :param escapadores_nuevos: list
        :return: None
        """
        enfermos_nuevos = enfermos_nuevos.split(",")
        escapadores_nuevos = escapadores_nuevos.split(",")
        total_multas = 0
        escape = 0
        enfermedad = 0
        salud_baja = 0
        if escapadores_nuevos != [""]:
            for nombre_criatura in escapadores_nuevos:
                criatura = self.criaturas[nombre_criatura.lower()]
                if random.random() < p.PROB_FISCALIZAR_ESCAPE:
                    print(f"Recibiste una multa porque {criatura.nombre} escapó")
                    total_multas += p.MULTA_ESCAPE
                    escape += 1
        if enfermos_nuevos != [""]:
            for nombre_criatura in enfermos_nuevos:
                criatura = self.criaturas[nombre_criatura.lower()]
                if random.random() < p.PROB_FISCALIZAR_ENFERMEDAD:
                    print(f"Recibiste una multa porque {criatura.nombre} enfermó")
                    total_multas += p.MULTA_ENFERMEDAD
                    enfermedad += 1
        for nombre_criatura in self.usuario_actual.criaturas:
            criatura = self.criaturas[nombre_criatura.lower()]
            if criatura.salud_actual == p.SALUD_MINIMA:
                print(f"Recibiste una multa porque {criatura.nombre} tiene su salud muy baja")
                total_multas += p.MULTA_SALUD_BAJA
                salud_baja += 1
        if escape == 0:
            print("No recibiste multas por criaturas que escaparon :D")
        if enfermedad == 0:
            print("No recibiste multas por criaturas que enfermaron :D")
        if salud_baja == 0:
            print("No recibiste multas por criaturas con salud muy baja :D")

        if total_multas > self.usuario_actual.sickles:
            print("No tienes el suficiente dinero para pagar tus multas")
            print("No se te cobrará el dinero pero perderás tu licencia")
            self.usuario_actual.licencia = False
        else:
            print(f"Se te descontaron {total_multas} Sickles en multas")
            self.usuario_actual.sickles -= total_multas
        print(f"Tu saldo actual es: {self.usuario_actual.sickles} Sickles")

    def pasar_dia(self):
        """
        Permite el paso al siguiente día
        :return: None
        """
        print("¡Has pasado al día siguiente!")
        print("*********************************************")
        print("Resumen de los eventos de hoy:\n")
        enfermos_nuevos = ""
        escapadores_nuevos = ""
        hambrientos_nuevos = ""
        for nombre_criatura in self.usuario_actual.criaturas:
            criatura = self.criaturas[nombre_criatura.lower()]
            criatura.cambiar_hambre()
            criat = criatura.enfermarse(self)
            if criat:
                if enfermos_nuevos == "":
                    enfermos_nuevos += criat.nombre
                else:
                    enfermos_nuevos += ","
                    enfermos_nuevos += criat.nombre
            criat = criatura.escaparse(self)
            if criat:
                if escapadores_nuevos == "":
                    escapadores_nuevos += criat.nombre
                else:
                    escapadores_nuevos += ","
                    escapadores_nuevos += criat.nombre
            if not criatura.comio_hoy:
                criatura.dias_sin_comer += 1
            criat = criatura.cambiar_hambre()
            if criat:
                if criat.nivel_hambre == "hambrienta":
                    if hambrientos_nuevos == "":
                        hambrientos_nuevos += criat.nombre
                    else:
                        hambrientos_nuevos += ","
                        hambrientos_nuevos += criat.nombre
        print(f"Criaturas que enfermaron hoy: {enfermos_nuevos}")
        print(f"Criaturas que escaparon hoy: {escapadores_nuevos}")
        print(f"Criaturas hambrientas desde hoy: {hambrientos_nuevos}")
        for nombre_criatura in self.usuario_actual.criaturas:
            criatura = self.criaturas[nombre_criatura.lower()]
            if criatura.estado_salud:
                criatura.salud_actual -= p.DISMINUCION_SALUD_POR_DIA_ENFERMO
                print(f"{criatura.nombre} perdió salud por enfermedad :(")
            if criatura.nivel_hambre == "hambrienta":
                criatura.salud_actual -= p.DISMINUCION_SALUD_POR_DIA_HAMBRE
                print(f"{criatura.nombre} perdió salud por hambre :(")
        print("*********************************************")
        self.usuario_actual.energia_actual = self.usuario_actual.energia
        self.calcular_aprobacion()
        self.pagar()
        self.fiscalizar(enfermos_nuevos, escapadores_nuevos)
        for nombre_criatura in self.usuario_actual.criaturas:
            criatura = self.criaturas[nombre_criatura.lower()]
            criatura.habilidad_comienzo_dia(self)
            actualizar_datos_criaturas(criatura, p.RUTA_CRIATURAS)
        print(f"Además recuperas tu energía total ({self.usuario_actual.energia_actual})")
        actualizar_datos_magizoologo(self.usuario_actual, p.RUTA_MAGIZOOLOGOS)


