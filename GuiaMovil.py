
opcion = input("a - Android i - Ios\n")

movil_ideal = "ninguno"

if opcion == "a":
    opcion = input("tienes dinero? s/n\n")

    if opcion == "s":
        opcion = input("te importa la camara? s/n\n")

        if opcion == "s":
            movil_ideal = "Pixel supercamara"

        else:
            movil_ideal = "android calidad precio xiaomi"

    else:
        movil_ideal = "android de 100€"

elif opcion == "i":
    opcion = input("tienes dinero? s/n\n")

    if opcion == "s":
        movil_ideal = "Iphone ultra pro max"

    else:
        movil_ideal = "Iphone de segunda mano"

print("tu movil ideal es:\n{}".format(movil_ideal))
#no hace falta usar format ("tu movil idea es" + movil_ideal) tambien funca