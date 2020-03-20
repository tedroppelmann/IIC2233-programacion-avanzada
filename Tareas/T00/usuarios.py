
import os
import prograpost
import seguidores

ruta_usuarios = os.path.join("usuarios.csv")
ruta_seguidores = os.path.join("seguidores.csv")


def agregar():
    while True:
        usuario = input("Ingrese el nuevo nombre de usuario:")
        if len(usuario) < 8:
            print("Error. El nombre usuario debe superar los 8 caracteres. Intente nuevamente.")
        elif usuario.isalnum() and usuario.isdigit() == False and usuario.isalpha() == False:
            file = open(ruta_usuarios)
            usuarios = []
            for line in file:
                usuarios.append(line.rstrip())
            file.close()
            if usuario in usuarios:
                    print("El nombre de usuario ya existe. Intente otro.")
            else:
                file2 = open(ruta_usuarios, "a")
                file2.write(str(usuario) + "\n")
                file2.close()
                file3 = open(ruta_seguidores, "a")
                file3.write(str(usuario) + "\n")
                file3.close()
                print("Usuario agregado exitosamente!")
                menu_usuario(usuario)
                return False
        else:
            print("Error. El nombre de usuario debe contener números y letras."
                  " Intente nuevamente.")

def ingresar():
    usuario = input("Ingrese el nombre de usuario:")
    file = open(ruta_usuarios)
    lines = file.readlines()
    file.close()
    if str(usuario + "\n") in lines:
        menu_usuario(usuario)
    else:
        print("El nombre de usuario no existe.")

def menu_usuario(usuario):
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