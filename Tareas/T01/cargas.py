
from collections import defaultdict
from magizoologos import Docencio, Tareo, Hibrido
from criaturas import Augurey, Niffler, Erkling
from alimentos import TartaDeMelaza, HigadoDeDragon, BuenueloDeGusarajo
import parametros as p



def cargar_magizoologos(ruta_archivo_magizoologos):

    magizoologos = defaultdict(lambda: "El Magizoólogo no existe.")
    with open(ruta_archivo_magizoologos, "r", encoding = "utf-8") as file:
        for line in file.readlines():
            nombre, tipo, sickles, criaturas, alimentos, licencia, nivel_magico, destreza\
            ,energia, responsabilidad, habilidad_especial = line.strip().split(",")
            criaturas = criaturas.split(";")
            alimentos = alimentos.split(";")

            if tipo == "Docencio":
                magizoologos[nombre.lower()] = Docencio(nombre, tipo, sickles, criaturas, alimentos,
                                                   licencia, nivel_magico, destreza, energia,
                                                   responsabilidad, habilidad_especial)

            elif tipo == "Tareo":
                magizoologos[nombre.lower()] = Tareo(nombre, tipo, sickles, criaturas, alimentos,
                                                licencia, nivel_magico, destreza, energia,
                                                responsabilidad, habilidad_especial)

            elif tipo == "Híbrido":
                magizoologos[nombre.lower()] = Hibrido(nombre, tipo, sickles, criaturas, alimentos,
                                             licencia, nivel_magico, destreza, energia,
                                             responsabilidad, habilidad_especial)

    return magizoologos


def cargar_criaturas(ruta_archivo_criaturas):

    criaturas = defaultdict(lambda: "La criatura no existe.")
    with open(ruta_archivo_criaturas, "r", encoding="utf-8") as file:
        for line in file.readlines():
            nombre, tipo, nivel_magico, probabilidad_escape, probabilidad_enfermarse\
                , estado_salud, estado_escape, salud_total, salud_actual, nivel_hambre\
                , nivel_agresividad, dias_sin_comer, nivel_cleptomania = line.strip().split(",")

            if tipo == "Augurey":
                criaturas[nombre.lower()] = Augurey(nombre, tipo, nivel_magico, probabilidad_escape,
                                            probabilidad_enfermarse , estado_salud, estado_escape,
                                            salud_total, salud_actual, nivel_hambre,
                                            nivel_agresividad, dias_sin_comer, nivel_cleptomania,
                                                    )

            elif tipo == "Niffler":
                criaturas[nombre.lower()] = Niffler(nombre, tipo, nivel_magico, probabilidad_escape,
                                            probabilidad_enfermarse , estado_salud, estado_escape,
                                            salud_total, salud_actual, nivel_hambre,
                                            nivel_agresividad, dias_sin_comer, nivel_cleptomania)

            elif tipo == "Erkling":
                criaturas[nombre.lower()] = Erkling(nombre, tipo, nivel_magico, probabilidad_escape,
                                            probabilidad_enfermarse, estado_salud, estado_escape,
                                            salud_total, salud_actual, nivel_hambre,
                                            nivel_agresividad, dias_sin_comer, nivel_cleptomania)

    return criaturas

def cargar_alimentos():

    alimentos = defaultdict(lambda: "El alimento no existe.")

    alimentos["Tarta de Melaza"] = TartaDeMelaza("Tarta de Melaza", p.SALUD_TARTA_MELAZA,
                                                p.PRECIO_TARTA_MELAZA)
    alimentos["Hígado de Dragón"] = HigadoDeDragon("Hígado de Dragón", p.SALUD_HIGADO_DRAGON,
                                                   p.PRECIO_HIGADO_DRAGON)
    alimentos["Buñuelo de Gusarajo"] = BuenueloDeGusarajo("Buñuelo de Gusarajo",
                                                          p.SALUD_BUNUELO_GUSARAJO,
                                                          p.PRECIO_BUNUELOS_GUSARAJO)
    return alimentos
