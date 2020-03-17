
import os
import prograpost
import seguidores

ruta_usuarios = os.path.join("usuarios.csv")
ruta_segudiores = os.path.join("seguidores.csv")


def agregar(usuario):
    file = open(ruta_usuarios)
    for line in file:
        if line.rstrip() == usuario:
            print("El nombre de usuario ya existe.")
            file.close()
            return
    file2 = open(ruta_usuarios, "a")
    file2.write(str(usuario) + "\n")
    file2.close()
    file3 = open(ruta_segudiores, "a")
    file3.write(str(usuario)+ "\n")
    file3.close()
    print("Usuario agregado exitosamente!")


def ingresar(usuario):
    file = open(ruta_usuarios)
    lines = file.readlines()
    file.close()
    if str(usuario + "\n") in lines:
        while True:
            print("Bienvenido " + str(usuario) + ". Elija un menú:")
            print("[1] Menú de prograpost")
            print("[2] Menú de seguidores")
            print("[0] Regresar al menú de inicio")
            respuesta = input("Indique su opción (0, 1 o 2):")
            if respuesta == str(1):
                prograpost.menu(usuario)
            elif respuesta == str(2):
                seguidores.menu(usuario)
            elif respuesta == str(0):
                return False
            else:
                print("Input incorrecto. Intente nuevamente.")
    else:
        print("El nombre de usuario no existe. Intente nuevamente.")