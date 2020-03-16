
import sys

import usuarios

print("Bienvenido a DCCahuin!!")

def menu():
    while True:
        print("Seleccione una opción:")
        print("[1] Iniciar sesión")
        print("[2] Registrar usuario")
        print("[0] Salir")
        respuesta = input("Indique su opción (0, 1 o 2):")
        if respuesta == str(1):
            nombre = input("Ingrese el nombre de usuario:")
            usuarios.ingresar(nombre)
        elif respuesta == str(2):
            nombre = input("Indique el nuevo nombre de usuario:")
            usuarios.agregar(nombre)
        elif respuesta == str(0):
            sys.exit()
        else:
            print("Input incorrecto. Intente nuevamente.")

menu()