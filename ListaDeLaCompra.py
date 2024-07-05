
print("bienvenido al programa de la lista de la compra")

lista = []
item = None
respuesta = None


while len(lista) < 3:

    item = input("que desea comprar? ([q] para salir e imprimir lista)")

    if item == "q":
        print(lista, "\nHasta otra")
        exit()

    elif item in lista:
        print("\n{} ya esta en la lista\n".format(item))

        if (input("¿Quiere añadir {} a la lista de nuevo? [S/N]\n".format(item))) == "S":
            lista.append(item)
            print("\n{} añadido a la lista\n".format(item))

    respuesta = ""
    while respuesta != "s" and respuesta != "n":
        respuesta = input("Seguro que quiere añadir {}? [s]i, [n]o".format(item))

    if respuesta == "s":
        lista.append(item)
        print("se ha añadiddo {} a la lista".format(item), "\n", lista)

    elif respuesta == "n":
        print("no se ha añadido nada a la lista")


if len(lista) >= 3:
    print("la lista de la compra es: {}, no se admiten mas elementos".format(lista))
    exit()