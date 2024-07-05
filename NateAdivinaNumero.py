import random

numero_ganador = random.randint(1, 10)
numero_elegido = int(input("elige un numero: "))

if numero_elegido == numero_ganador:
    print("has ganado")

if numero_elegido > 10:
    print("es demasiado grande, es entre 1 y 10")
if numero_elegido < 1:
    print("es demasiado pequeño, es entre 1 y 10")
if numero_elegido == 666:
    print("putos santanicos")
if numero_elegido == -666:
    print("y ademas, has elegido el numero de la bestia en negativo, tremendamente maligno")

print("el numero ganador era: {}".format(numero_ganador))