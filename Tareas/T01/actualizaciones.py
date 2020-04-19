
def agregar_magizoologo(manizoologo, ruta_archivo_magizoologos):
    """
    Agrega un magizoologo nuevo al archivo .csv de magizoologos
    :param manizoologo: Magizoologo
    :param ruta_archivo_magizoologos: str
    :return: None
    """
    criaturas = ";".join(manizoologo.criaturas)
    alimentos = ";".join(manizoologo.alimentos)
    with open(ruta_archivo_magizoologos, "a", encoding="utf-8") as file:
        file.write(manizoologo.nombre + "," + manizoologo.tipo + "," + str(manizoologo.sickles) +
                   "," + criaturas + "," + alimentos + "," +str(manizoologo.licencia) +
                   "," + str(manizoologo.nivel_magico) + "," + str(manizoologo.destreza) +
                   "," + str(manizoologo.energia) + "," + str(manizoologo.responsabilidad) +
                   "," + str(manizoologo.habilidad_especial) +"\n")

def agregar_criatura(criatura, ruta_archivo_magizoologos):
    """
    Agrega una criatura nueva al archivo .csv de criaturas
    :param criatura: Criatura
    :param ruta_archivo_magizoologos: str
    :return: None
    """
    with open(ruta_archivo_magizoologos, "a", encoding="utf-8") as file:
        file.write(criatura.nombre + "," + criatura.tipo + "," + str(criatura.nivel_magico) +
                   "," + str(criatura.probabilidad_escape) + "," +
                   str(criatura.probabilidad_enfermarse) + "," + str(criatura.estado_salud) +
                   "," + str(criatura.estado_escape) + "," + str(criatura.salud_total) + "," +
                   str(criatura.salud_total) + "," + str(criatura.nivel_hambre) + ","
                   + str(criatura.nivel_agresividad) + "," + str(criatura.dias_sin_comer) + "," +
                   str(criatura.nivel_cleptomania) + "\n")

def actualizar_datos_magizoologo(manizoologo, ruta_archivo_magizoologos):
    """
    Permite actualizar cualquier cambio en el archivo .csv de magizoologos
    :param manizoologo: Magizoologo
    :param ruta_archivo_magizoologos: str
    :return: None
    """
    if "" in manizoologo.alimentos:
        manizoologo.alimentos.remove("")
    alimentos_nuevos = ";".join(manizoologo.alimentos)
    criaturas_nuevas = ";".join(manizoologo.criaturas)
    filas = dict()

    with open(ruta_archivo_magizoologos, "r", encoding="utf-8") as file:
        lineas = file.readlines()
        for line in lineas:
            nombre, tipo, sickles, criaturas, alimentos, licencia, nivel_magico, destreza,\
            energia, responsabilidad, habilidad_especial = line.strip().split(",")
            filas[nombre] = line

    key_list = list(filas.keys())

    with open(ruta_archivo_magizoologos, "w", encoding="utf-8") as file2:
        for key in key_list:
            if key != manizoologo.nombre:
                file2.write(filas[key])
            elif key == manizoologo.nombre:
                file2.write(manizoologo.nombre + "," + manizoologo.tipo + "," +
                            str(manizoologo.sickles) + "," + criaturas_nuevas
                            + "," + alimentos_nuevos + "," + str(manizoologo.licencia) + "," +
                            str(manizoologo.nivel_magico) + "," + str(
                    manizoologo.destreza) + "," +
                            str(manizoologo.energia) + "," + str(
                    manizoologo.responsabilidad) + ","
                            + str(manizoologo.habilidad_especial) + "\n")

def actualizar_datos_criaturas(criatura, ruta_archivo_criaturas):
    """
    Permite actualizar cualquier cambio en el archivo .csv de criaturas
    :param criatura: Criatura
    :param ruta_archivo_criaturas: str
    :return: None
    """
    filas = dict()
    with open(ruta_archivo_criaturas, "r", encoding="utf-8") as file:
        lineas = file.readlines()
        for line in lineas:
            nombre, tipo, nivel_magico, probabilidad_escape, probabilidad_enfermarse, estado_salud,\
            estado_escape, salud_total, salud_actual, nivel_hambre, nivel_agresividad,\
            dias_sin_comer, nivel_cleptomania = line.strip().split(",")
            filas[nombre] = line

    key_list = list(filas.keys())

    with open(ruta_archivo_criaturas, "w", encoding="utf-8") as file2:
        for key in key_list:
            if key != criatura.nombre:
                file2.write(filas[key])
            elif key == criatura.nombre:
                file2.write(criatura.nombre + "," + criatura.tipo + "," + str(criatura.nivel_magico)
                            + "," + str(criatura.probabilidad_escape) + "," +
                            str(criatura.probabilidad_enfermarse) + "," + str(criatura.estado_salud)
                            + "," + str(criatura.estado_escape) + "," + str(criatura.salud_total) +
                            "," + str(criatura.salud_actual) + "," + str(criatura.nivel_hambre) +
                            "," + str(criatura.nivel_agresividad) + "," +
                            str(criatura.dias_sin_comer) + "," + str(criatura.nivel_cleptomania)
                            + "\n")

def str_bool(string):
    """
    Transforma un string a un bool
    :param string: str
    :return: bool
    """
    if string == "True":
        return True
    else:
        return False