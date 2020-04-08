
import sys

def menu_inicio(DCC):
    while True:
        print("***** MENÚ DE INICIO *****")
        print("Selecciones una opción:")
        print("[1] Crear Magizoólogo")
        print("[2] Cargar Magizoólogo")
        print("[0] Salir")
        respuesta = input("Indique una opción (1, 2 o 0):")
        if respuesta == "1":
            DCC.crear_magizoologo()
        elif respuesta == "2":
            DCC.cargar_magizoologo()
        elif respuesta == "0":
            print("Adiós ¡Vuelve pronto!")
            sys.exit()
        else:
            print("ERROR. Intente nuevamente.")

def menu_error(DCC):
    while True:
        print("[1] Intentar de nuevo \n[2] Volver atrás \n[0] Salir")
        respuesta = input("Ingrese una opción (1, 2 o 0):")
        if respuesta == "1":
            return True
        elif respuesta == "2":
            menu_inicio(DCC)
        elif respuesta == "0":
            sys.exit()

def menu_acciones(DCC):
    while True:
        print("***** MENÚ DE ACCIONES *****")
        print("Selecciones una opción:")
        print("[1] Menú cuidar DCCriaturas")
        print("[2] Menú DCC")
        print("[3] Pasar al día siguiente")
        print("[4] Volver atrás")
        print("[0] Salir")
        respuesta = input("Indique una opción (1, 2 o 0):")
        if respuesta == "1":
            menu_cuidar(DCC)
        elif respuesta == "2":
            menu_dcc(DCC)
        elif respuesta == "3":
            pass
        elif respuesta == "4":
            menu_inicio(DCC)
        elif respuesta == "0":
            print("Adiós ¡Vuelve pronto!")
            sys.exit()
        else:
            print("ERROR. Intente nuevamente.")

def menu_cuidar(DCC):
    while True:
        print("***** MENÚ DE CUIDAR DCCRIATURAS *****")
        print("Selecciones una opción:")
        print("[1] Alimentar DCCriatura")
        print("[2] Recuperar DCCriatura")
        print("[3] Sanar DCCcriatura")
        print("[4] Usar habilidad especial")
        print("[5] Volver atrás")
        print("[0] Salir")
        respuesta = input("Indique una opción (1, 2 o 0):")
        if respuesta == "1":
            DCC.crear_magizoologo()
        elif respuesta == "2":
            DCC.cargar_magizoologo()
        elif respuesta == "0":
            print("Adiós ¡Vuelve pronto!")
            sys.exit()
        else:
            print("ERROR. Intente nuevamente.")

def menu_dcc(DCC):
    while True:
        print("***** MENÚ DE DCC *****")
        print("Selecciones una opción:")
        print("[1] Adoptar una DCCriatura")
        print("[2] Comprar alimentos")
        print("[3] Ver estado de Magizoólogo y DCCriaturas")
        print("[4] Volver atrás")
        print("[0] Salir")
        respuesta = input("Indique una opción (1, 2 o 0):")
        if respuesta == "1":
            DCC.usuario_actual.adoptar(DCC)
        elif respuesta == "2":
            pass
        elif respuesta == "0":
            print("Adiós ¡Vuelve pronto!")
            sys.exit()
        else:
            print("ERROR. Intente nuevamente.")



