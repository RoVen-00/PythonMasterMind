edad = int(input("dígame su edad: "))
tipo_de_carnet = (input("Indique su tipo de carnet: (e: Estudiante/p: Pensionista/f: Familia numerosa/n: Nada): "))
if (25 <= edad <= 35 and tipo_de_carnet == "e") or \
        edad <= 10 or \
        (edad >= 65 and tipo_de_carnet == "p") or \
        tipo_de_carnet == "f":

    print("Se te aplica el descuento")
else:
    print("no se te aplica el descuento")
