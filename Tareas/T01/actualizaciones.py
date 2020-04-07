
def agregar_magizoologo(manizoologo, ruta_archivo_magizoologos):
    criaturas = ";".join(manizoologo.criaturas)
    alimentos = ";".join(manizoologo.alimentos)
    with open(ruta_archivo_magizoologos, "a", encoding="utf-8") as file:
        file.write(manizoologo.nombre + "," + manizoologo.tipo + "," + str(manizoologo.sickles) +
                   "," + criaturas + "," + alimentos + "," +str(manizoologo.licencia) +
                   "," + str(manizoologo.nivel_magico) + "," + str(manizoologo.destreza) +
                   "," + str(manizoologo.energia) + "," + str(manizoologo.responsabilidad) +
                   "," + str(manizoologo.habilidad_especial) +"\n")

def agregar_criatura(criatura, ruta_archivo_magizoologos):

    with open(ruta_archivo_magizoologos, "a", encoding="utf-8") as file:
        file.write(criatura.nombre + "," + criatura.tipo + "," + str(criatura.nivel_magico) +
                   "," + str(criatura.probabilidad_escape) + "," +
                   str(criatura.probabilidad_enfermarse) + "," + str(criatura.estado_salud) +
                   "," + str(criatura.estado_escape) + "," + str(criatura.salud_total) + "," +
                   str(criatura.salud_total) + "," + str(criatura.nivel_hambre) + ","
                   + str(criatura.nivel_agresividad) + "," + str(criatura.dias_sin_comer) + "," +
                     str(criatura.nivel_cleptomania) + "\n")
