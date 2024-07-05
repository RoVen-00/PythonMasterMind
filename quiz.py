
titulo = "bienvenido al test sobre el queso"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

puntuacion = 0

opcion = input("¿Que haces cuando ves una tabla de quesos?\n"
               "A - Salgo corriendo \n"
               "B - Pruebo uno de los quesos o incluso varios \n"
               "C - No puedo evitar deborarla")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones posibles son A, B, C, largo de aqui graciosillo")
    exit()

opcion = input("¿Como te gusta la hamburguesa?\n"
               "A - Sin queso\n"
               "B - Con queso\n"
               "C - Pan y queso\n")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones posibles son A, B, C")
    exit()

opcion = input("¿Eres intolerante a la lactosa?"
               "A - Si\n"
               "B - A veces\n"
               "C - No\n")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones posibles son A, B, C")
    exit()

if puntuacion >= 25:
    print("felicidades te flipa el queso")
elif puntuacion >= 15:
    print("te gusta el queso")
else:
    print("definitivamente no te gusta el queso")