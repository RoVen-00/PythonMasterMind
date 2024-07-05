numeros_de_usuario = []

numero_introducido = int(input("introduzca un numero de la lista: "))
numeros_de_usuario.append(numero_introducido)

while input("¿desea introducir mas numeros [S/N] ") == "s":
    numero_introducido= int(input("introduzca un numero en la lista: "))
    numeros_de_usuario.append(numero_introducido)

numero_pequeno = numeros_de_usuario[0]
numero_grande = numeros_de_usuario[0]

for numero in numeros_de_usuario[1:]:
    if numero_pequeno > numero:
        numero_pequeno = numero

    if numero_grande < numero:
        numero_grande = numero

print("numero grande: {}, numero pequeño {}".format(numero_grande, numero_pequeno))