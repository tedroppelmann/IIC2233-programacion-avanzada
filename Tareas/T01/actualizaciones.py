

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

def actualizar_datos(manizoologo, ruta_archivo_magizoologos):

    alimentos_nuevos = ";".join(manizoologo.alimentos)
    criaturas_nuevas = ";".join(manizoologo.criaturas)
    print(criaturas_nuevas)

    with open(ruta_archivo_magizoologos, "r", encoding="utf-8") as file:
        lineas = file.readlines()
        nombres = []
        for linea in lineas:
            columnas = linea.split(",")
            nombres.append(columnas[0])



    with open(ruta_archivo_magizoologos, "w", encoding="utf-8") as file2:
        for linea in lineas:
            print(str(manizoologo.nombre))
            for i in nombres:
                if str(manizoologo.nombre) == i:
                    file2.write(linea)
                    print("!")
                else:
                    file2.write(manizoologo.nombre + "," + manizoologo.tipo + "," +
                           str(manizoologo.sickles) + "," + criaturas_nuevas
                           + "," + alimentos_nuevos + "," + str(manizoologo.licencia) + "," +
                           str(manizoologo.nivel_magico) + "," + str(manizoologo.destreza) + "," +
                           str(manizoologo.energia) + "," + str(manizoologo.responsabilidad) + ","
                           + str(manizoologo.habilidad_especial) +"\n")
