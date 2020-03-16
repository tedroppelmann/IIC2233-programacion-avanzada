
import os

import prograpost

ruta_usuarios = os.path.join("usuarios.csv")

file = open(ruta_usuarios, "a")
file.write("\n")
file.close()

def agregar(nombre):
    file = open(ruta_usuarios)
    for line in file:
        if line.rstrip() == nombre:
            print("El nombre de usuario ya existe.")
            file.close()
            return
    file2 = open(ruta_usuarios, "a")
    file2.write(str(nombre) + "\n")
    file2.close()
    print("Usuario agregado exitosamente!")


def ingresar(nombre):
    file = open(ruta_usuarios)
    lines = file.readlines()
    file.close()
    if str(nombre + "\n") in lines:
        while True:
            print("Bienvenido " + str(nombre) + ". Elija un menú:")
            print("[1] Menú de prograpost")
            print("[2] Menú de seguidores")
            print("[0] Regresar al menú anterior")
            respuesta = input("Indique su opción (0, 1 o 2):")
            if respuesta == str(1):
                prograpost.menu()
                return False
            elif respuesta == str(2):
                print("SEGUIDORES")
                return False
            elif respuesta == str(0):
                return False
            else:
                print("Input incorrecto. Intente nuevamente.")
    else:
        print("El nombre de usuario no existe. Intente nuevamente.")



