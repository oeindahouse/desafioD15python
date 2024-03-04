def obtener_opcion_menu() -> int:
    """
    obtener_opcion_menu _summary_

    _extended_summary_

    :return: _description_
    :rtype: int
    """


    OPCIONES_MENU = ['1', '2', '3', '4', '5']
    opcion_menu: int=0
    while type(opcion_menu) == int and opcion_menu not in OPCIONES_MENU:
        opcion_menu_aux = input("ingrese una opcion del menu (1, 2, 3, 4, 5): ")
        #opcion_menu = int(opcion_menu_aux) if opcion_menu_aux.isdigit() and opcion_menu_aux in OPCIONES_MENU else 0
        if opcion_menu_aux.isdigit() and opcion_menu_aux in OPCIONES_MENU:
            opcion_menu = opcion_menu_aux
        else:
            print("ingresar opcion valida")
            
    return opcion_menu

def imprimir_opciones_menu(funcion_imprimir = None, param_funcion = None):
    """
    imprimir_opciones_menu _summary_

    _extended_summary_
    """
    print("########## Agenda Py 1.0 ##########")
    print("que quieres hacer?")
    print('''
        \n
        1.- Ingresar nuevo contacto
        2.- Buscar contacto
        3.- Actualizar contacto
        4.- Eliminar contacto
        5.- Salir
        \n''')
    
    if funcion_imprimir is not None:
        funcion_imprimir(param_funcion)
    
    print("\n ######### Agenda Py 1.0 ########\n")