
import os
from datetime import date

ruta_posts = os.path.join("posts.csv")
ruta_seguidores = os.path.join("seguidores.csv")

def menu(usuario):
    while True:
        print("MENÚ DE PROGRAPOSTS")
        print("Elija una opción:")
        print("[1] Crear prograpost")
        print("[2] Eliminar prograpost")
        print("[3] Ver tus prograpost ")
        print("[4] Ver prograpost de tus seguidores")
        print("[5] Regresar al menú de inicio")
        respuesta = input("Indique su opción (1, 2, 3, 4 o 5):")
        if respuesta == str(1):
            crear(usuario)
        elif respuesta == str(2):
            eliminar(usuario)
        elif respuesta == str(3):
            ver_posts(usuario)
        elif respuesta == str(4):
            ver_posts_seguidores(usuario)
        elif respuesta == str(5):
            return False
        else:
            print("Input incorrecto. Intente nuevamente.")

def crear(usuario):
    mensaje = input("Escriba el mensaje:")
    if len(mensaje) < 1:
        print("Post vacío. Intente nuevamente.")
    elif len(mensaje) > 140:
        print("Post supera largo máximo. Intente nuevamente")
    else:
        file = open(ruta_posts, "a")
        today = date.today()
        file.write(str(usuario) + ",")
        file.write(str(today.strftime("%Y/%m/%d")) + ",")
        file.write(mensaje + "\n")
        file.close()
        print("Prograpost publicado exitosamente!")

def ver_posts(usuario):
    file = open(ruta_posts)
    mensajes = []
    for line in file:
        linea = line.rstrip()
        columnas = linea.split(",")
        texto = ",".join(columnas[2:])
        lista = [columnas[1], texto]
        if columnas[0] == usuario:
            mensajes.append(lista)
    file.close()
    while True:
        if len(mensajes) == 0:
            print("El usuario no tiene post publicados.")
            return False
        print("Desea ordenar los posts de forma: ")
        print("[1] Ascendente")
        print("[2] Descendente")
        orden = input("Indique su opción (1 o 2):")
        if orden == str(1):
            mensajes.sort()
            print("FECHA, MENSAJE")
            for m in mensajes:
                print(m)
            return False
        elif orden == str(2):
            print("FECHA, MENSAJE")
            mensajes.sort(reverse = True)
            for m in mensajes:
                print(m)
            return False
        else:
            print("Input incorrecto. Intente nuevamente.")

def eliminar(usuario):
    file = open(ruta_posts)
    mensajes = []
    for line in file:
        linea = line.rstrip()
        columnas = linea.split(",")
        texto = ",".join(columnas[2:])
        lista = [columnas[1], texto]
        if columnas[0] == usuario:
            mensajes.append(lista)
    file.close()
    while True:
        if len(mensajes) == 0:
            print("El usuario no tiene post publicados.")
            return False
        print("Estos son tus post publicados:")
        for i in range(len(mensajes)):
            print(str(i + 1))
            print(mensajes[i])
        numero = int(input("¿Que post desea borrar? Elija el número de publicación (1, 2 , 3, ...):"))
        if numero >0 and numero <= len(mensajes):
            linea = [usuario, mensajes[numero-1][0],mensajes[numero-1][1]]
            linea =  ",".join(linea)
            file = open(ruta_posts)
            lineas = file.readlines()
            file.close()
            file2 = open(ruta_posts, "w")
            for line in lineas:
                if line.rstrip() != str(linea):
                    file2.write(line)
            file.close()
            print("Post eliminado exitosamente")
            return False
        else:
            print("Número inválido. Intenta nuevamente.")

def ver_posts_seguidores(usuario):
    file = open(ruta_seguidores)
    seguidores = []
    for line in file:
        linea = line.rstrip()
        columna = linea.split(",")
        if columna[0] == usuario:
            for i in range(1,len(columna)):
                seguidores.append(columna[i])
    file.close()
    file = open(ruta_posts)
    posts = []
    for line in file:
        linea = line.rstrip()
        columna = linea.split(",")
        cuerpo = ",".join(columna[2:])
        lista = [columna[1], columna[0], cuerpo]
        if columna[0] in seguidores:
            posts.append(lista)
    file.close()
    while True:
        if len(posts) == 0:
            print("No hay posts que mostrar.")
            return False
        print("Desea ordenar los posts de forma: ")
        print("[1] Ascendente")
        print("[2] Descendente")
        orden = input("Indique su opción (1 o 2):")
        if orden == str(1):
            posts.sort()
            print("FECHA, USUARIO, MENSAJE")
            for m in posts:
                print(m)
            return False
        elif orden == str(2):
            print("FECHA, USUARIO, MENSAJE")
            posts.sort(reverse=True)
            for m in posts:
                print(m)
            return False
        else:
            print("Input incorrecto. Intente nuevamente.")