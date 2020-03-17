
import sys
import usuarios

print("Bienvenido a DCCahuin!!")

def menu():
    while True:
        print("MENÚ DE INICIO")
        print("Seleccione una opción:")
        print("[1] Iniciar sesión")
        print("[2] Registrar usuario")
        print("[0] Salir")
        respuesta = input("Indique su opción (0, 1 o 2):")
        if respuesta == str(1):
            usuario = input("Ingrese el nombre de usuario:")
            usuarios.ingresar(usuario)
        elif respuesta == str(2):
            usuario = input("Indique el nuevo nombre de usuario:")
            usuarios.agregar(usuario)
        elif respuesta == str(0):
            sys.exit()
        else:
            print("Input incorrecto. Intente nuevamente.")

menu()