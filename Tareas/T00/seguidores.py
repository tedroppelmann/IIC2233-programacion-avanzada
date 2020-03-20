
import os

ruta_seguidores = os.path.join("seguidores.csv")
ruta_usuarios = os.path.join("usuarios.csv")

def menu(usuario):
    while True:
        print("MENÚ DE SEGUIDORES")
        print("Elija una opción:")
        print("[1] Seguir a un usuario")
        print("[2] Dejar de seguir a un usuario")
        print("[0] Regresar al menú de inicio")
        respuesta = input("Indique su opción (1, 2, o 0):")
        if respuesta == str(1):
            seguir(usuario)
        elif respuesta == str(2):
            dejar(usuario)
        elif respuesta == str(0):
            return False

def seguir(usuario):
    file = open(ruta_seguidores)
    lineas = file.readlines()
    file.close()
    seguidor = input("Ingrese usuario a seguir:")
    file1 = open(ruta_usuarios)
    linea1 = ""
    linea_nueva = ""
    lines = file1.readlines()
    file1.close()
    if usuario == seguidor:
        print("No puedes seguirte a ti mismo. Intenta nuevamente.")
    elif str(seguidor) + "\n" in lines and \
                    lista_seguidores(usuario, seguidor) \
                    == False:
        for line in lineas:
            linea = line.rstrip()
            columnas = linea.split(",")
            if columnas[0] == usuario:
                linea1 = ",".join(columnas)
                columnas.append(seguidor)
                linea_nueva = ",".join(columnas)
        file = open(ruta_seguidores, "w")
        for line in lineas:
            if line.rstrip() != linea1:
                file.write(line)
            else:
                file.write(linea_nueva + "\n")
        file.close()
        print("El usuario " + str(seguidor)
              + " fue seguido con éxito!")
    elif lista_seguidores(usuario, seguidor):
        print("Ya sigues a " + str(seguidor)
              + ". Intenta nuevamente.")
    else:
        print("Nombre de usuario no existe. Intente nuevamente.")

def lista_seguidores(usuario, seguidor):
    file = open(ruta_seguidores)
    for line in file:
        linea = line.rstrip()
        columnas = linea.split(",")
        if columnas[0] == usuario and seguidor in columnas[1:]:
            return True
    return False

def dejar(usuario):
    file = open(ruta_seguidores)
    lineas = file.readlines()
    file.close()
    linea_1 = ""
    linea_nueva = ""
    seguidor = input("Ingrese a quién desea dejar de seguir:")
    if lista_seguidores(usuario, seguidor):
        for line in lineas:
            linea = line.rstrip()
            columnas = linea.split(",")
            if columnas[0] == usuario:
                linea_1 = ",".join(columnas)
                columnas.remove(seguidor)
                linea_nueva = ",".join(columnas)
        file = open(ruta_seguidores, "w")
        for line in lineas:
            if line.rstrip() != linea_1:

                file.write(line)
            else:
                file.write(str(linea_nueva) + "\n")
        file.close()
        print("Dejaste de seguir a " + str(seguidor)
              + " con éxito.")
    elif not lista_seguidores(usuario, seguidor):
        print("Tu no sigues a " + str(seguidor)
              + ". Intenta nuevamente.")