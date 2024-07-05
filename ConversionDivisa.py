
dolar_euro = 0.91
libra_euro = 1.18

opcion = input("¿que desea hacer?\n"
               "A - convertir dolar a euro\n"
               "B - convetir euro a dolar\n"
               "C - converit libra a euro\n"
               "D - converitr euro a libra\n")



texto_usuario = "intruduzca la cantidad de {} a convertir: "

if opcion == "A":
    cantidad_de_dinero = float(input(texto_usuario.format("dolares")))
    print("la cantidad en euros es {}".format(cantidad_de_dinero * dolar_euro))

elif opcion == "B":
    cantidad_de_dinero = float(input(texto_usuario.format("euros")))
    print("la cantidad en dolares es {}".format(cantidad_de_dinero / dolar_euro))

elif opcion == "C":
    cantidad_de_dinero = float(input(texto_usuario.format("libras")))
    print("la cantidad en euros es {}".format(cantidad_de_dinero * libra_euro))

elif opcion == "D":
    cantidad_de_dinero = float(input(texto_usuario.format("euros")))
    print("la cantidad en libras es {}".format(cantidad_de_dinero / libra_euro))

else:
    print("no ha elegido ninguna opcion valida")

