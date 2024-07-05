import os
lista_compra = []
SALIR = "SALIR"
# PRODUCTOS_SUPERMERCADO = ["pollo", "lechuga"]
FICHERO = "compra.txt"
RUTA_FICHERO = "/Python MasterMind"


def preguntar_producto_usuario():

    return input("\nIntroduce un producto o escribe {} para salir: ".format(SALIR))
    #producto_elegido = input("\nIntroduce un producto o escribe {} para salir: ".format(SALIR))
    #while producto_elegido.lower() not in PRODUCTOS_SUPERMERCADO and producto_elegido != SALIR:
        # .lower() hace que el programa no sea case sensitive y no te diga que no hay X producto si lo escribes en
        # mayuscula
        #print("El supermercado no tiene ese producto")
        #producto_elegido = input("\nIntroduce un producto o escribe {} para salir: ".format(SALIR))
    #return producto_elegido


def escribir_fichero(lista_compra):

    # Esta version tiene dos versiones diferntes, una en la que te pregunta donde quieres guardar
    # la lista y otra donde la guarda automaticamente al salir en una ruta definida en una constante.
    # Ahora mismo se esta usando la automatica.
    # Si quieres usar la que pregunta descomenta la variable con el input de aqui abajo y comenta
    # arriba del todo FICHERO y RURA_FICHERO

    print("Tu lista de la compra se ha guardado automaticamente en " + RUTA_FICHERO + " con el nombre " + FICHERO)
    # fichero = input("En que fichero quieres guardar la lista?: ")
    """ Esta es una manera de hacer que te guarde la lista en un fichero.
    a = open(fichero + ".txt", "w")
    a.write("\n".join(lista_compra))
    a.close()
    """
    # esta es la manera pro de que te guarde el input en un fichero
    with open(FICHERO, "w") as el_fichero:
        # Dentro del parentesis sustituye FICHERO por fichero + ".txt" y descomenta la linea del input de este funcion
        el_fichero.write("\n".join(lista_compra))


def guardar_item_en_lista(lista_compra, item_a_guardar):

    if item_a_guardar.lower() in [producto.lower() for producto in lista_compra]:
        # Donde pone [producto.lower() for producto in lista_compra] tu tenias lista_compra.
        # Sirve para entre otras cosas que veras mas adelante para crear otra lista
        # con los productos en minuscula que tiene lista_compra. Lo hace en un for porque para saber que productos
        # tiene, necesita iterar lista_compra
        # Es un list comprehension de:
        # segunda_lista = []
        # for producto in lista_compra:
        #   segunda_lista.append(producto.lower())
        # Es importante que sepas que no vas a usar la variable segunda_lista para nada. Lo unico que necesitas
        # es que el programa mire con el for los productos de lista_compra
        print("El producto ya esta en la lista")
    else:
        lista_compra.append(item_a_guardar)


def cargar_o_crear_archivo():

    lista_compra = []
    if input("Queres cargar la ultima lista de la compra? [SI/NO]: ") == "SI":
        try:
            with open(FICHERO, "r") as el_fichero:
            # Dentro del parentesis sustituye FICHERO por fichero + ".txt" y descomenta la linea del input de este funcion
                lista_compra = el_fichero.read().split("\n")
            # compra.txt contiene una string (va a ir todo el texto en la misma linea) pero nosotros queremos que
            # que se muestre como una lista por lo que tenemos que hacerle un split por enters (/n)
        except FileNotFoundError:
            print("El archivo " + FICHERO + " no existe en" + RUTA_FICHERO + ". Se ha creado uno nuevo.")
    return lista_compra


def mostrar_lista(lista_compra):

    print("\n".join(lista_compra))
    return lista_compra


def main():

    lista_compra = cargar_o_crear_archivo()

    mostrar_lista(lista_compra)

    input_usuario = preguntar_producto_usuario()

    while input_usuario != SALIR:
        guardar_item_en_lista(lista_compra, input_usuario)
        mostrar_lista(lista_compra)
        input_usuario = preguntar_producto_usuario()

    escribir_fichero(lista_compra)


if __name__ == "__main__":
    main()

