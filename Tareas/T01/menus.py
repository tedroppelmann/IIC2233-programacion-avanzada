
import sys

def menu_inicio(dcc):
    while True:
        print("\n***** MENÚ DE INICIO *****")
        print("Selecciones una opción:")
        print("[1] Crear Magizoólogo")
        print("[2] Cargar Magizoólogo")
        print("[0] Salir")
        respuesta = input("Indique una opción (1, 2 o 0):")
        if respuesta == "1":
            dcc.crear_magizoologo()
        elif respuesta == "2":
            dcc.cargar_magizoologo()
        elif respuesta == "0":
            print("Adiós ¡Vuelve pronto!")
            sys.exit()
        else:
            print("ERROR. Intente nuevamente.")

def menu_error(dcc, menu_anterior):
    """
    Aparece cuando ocurre un error en el programa y permite volver al menu anterior
    :param dcc: Dcc
    :param menu_anterior: str
    :return: bool
    """
    while True:
        print("[1] Intentar de nuevo \n[2] Volver atrás \n[0] Salir")
        respuesta = input("Ingrese una opción (1, 2 o 0):")
        if respuesta == "1":
            return True
        elif respuesta == "2":
            menu_anterior(dcc)
        elif respuesta == "0":
            print("Adiós ¡Vuelve pronto!")
            sys.exit()

def menu_acciones(dcc):
    while True:
        print("\n***** MENÚ DE ACCIONES *****")
        print("Selecciones una opción:")
        print("[1] Menú cuidar DCCriaturas")
        print("[2] Menú DCC")
        print("[3] Pasar al día siguiente")
        print("[4] Volver atrás")
        print("[0] Salir")
        respuesta = input("Indique una opción (1, 2, 3, 4 o 0):")
        if respuesta == "1":
            menu_cuidar(dcc)
        elif respuesta == "2":
            menu_dcc(dcc)
        elif respuesta == "3":
            dcc.pasar_dia()
        elif respuesta == "4":
            menu_inicio(dcc)
        elif respuesta == "0":
            print("Adiós ¡Vuelve pronto!")
            sys.exit()
        else:
            print("ERROR. Intente nuevamente.")

def menu_cuidar(dcc):
    while True:
        print("\n***** MENÚ DE CUIDAR DCCRIATURAS *****")
        print("Selecciones una opción:")
        print("[1] Alimentar DCCriatura")
        print("[2] Recuperar DCCriatura")
        print("[3] Sanar DCCcriatura")
        print("[4] Usar habilidad especial")
        print("[5] Volver atrás")
        print("[0] Salir")
        respuesta = input("Indique una opción (1, 2, 3, 4, 5 o 0):")
        if respuesta == "1":
            dcc.usuario_actual.alimentar_criatura(dcc)
        elif respuesta == "2":
            dcc.usuario_actual.recuperar_criatura(dcc)
        elif respuesta == "3":
            dcc.usuario_actual.sanar_criatura(dcc)
        elif respuesta == "4":
            dcc.usuario_actual.usar_habilidad_especial(dcc)
        elif respuesta == "5":
            menu_acciones(dcc)
        elif respuesta == "0":
            print("Adiós ¡Vuelve pronto!")
            sys.exit()
        else:
            print("ERROR. Intente nuevamente.")

def menu_dcc(dcc):
    while True:
        print("\n***** MENÚ DE DCC *****")
        print("Selecciones una opción:")
        print("[1] Adoptar una DCCriatura")
        print("[2] Comprar alimentos")
        print("[3] Ver estado de Magizoólogo y DCCriaturas")
        print("[4] Volver atrás")
        print("[0] Salir")
        respuesta = input("Indique una opción (1, 2, 3, 4 o 0):")
        if respuesta == "1":
            dcc.usuario_actual.adoptar(dcc)
        elif respuesta == "2":
            dcc.usuario_actual.comprar_alimento(dcc)
        elif respuesta == "3":
            dcc.mostrar_estado()
        elif respuesta == "4":
            menu_acciones(dcc)
        elif respuesta == "0":
            print("Adiós ¡Vuelve pronto!")
            sys.exit()
        else:
            print("ERROR. Intente nuevamente.")