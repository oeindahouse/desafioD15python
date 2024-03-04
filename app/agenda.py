from app.modulos.menu.mod_menu import imprimir_opciones_menu, obtener_opcion_menu
from app.modulos.contacto.mod_contacto import mostrar_lista_contacto


def agenda():
    lista_contactos: list = []
    imprimir_opciones_menu(mostrar_lista_contacto, lista_contactos)
    opcion_menu = obtener_opcion_menu()
    

        