numeros_introducidos = input("introduzca los numeros separados por comas: ")
numeros_de_usuario = numeros_introducidos.split(",")
numeros_de_usuario_limpios = []

for numero in numeros_de_usuario:
    numeros_de_usuario_limpios.append(int(numero))

"""
numeros_de_usuario = [int(numero) for numero in numeros_de_usuario] 
a esta linea se le llama list comprehesion y lo que hace es sustituir a la linea 5 y 6, 
Puedes tambien condensar aqui la linea 2 de esta manera:
numeros_de_usuario = [int(numero) for numeros_introducidos.split(",")] 

A esto se le llama list comprehension
"""
numero_pequeno = numeros_de_usuario[0] #con [0] asumes que el primero de la lista es el mas pequeño
numero_grande = numeros_de_usuario[0]

for numero in numeros_de_usuario[1:]: #a esto se le llama filtrado de listas,
    # le estas diciendo que empiece a iterar a partir del segundo numero (porque el primero ya lo has puesto en las lineas 16 y 17
    #tambien puedes hacer [1:3] para que el for solo actue des de la posicion 2 a la 4
    if numero_pequeno > numero:
        numero_pequeno = numero

    elif numero_grande < numero:
        numero_grande = numero

#El bloque de la 16 a la 26 sirve para comparar los numeros a partir de la segunda posicion con el que hay en la primera
#asi es como va a ver el programa cual es el mayor y cual el menor. Es una manera muy forzada pero sirve.
print("numero grande: {}, numero pequeño {}".format(numero_grande, numero_pequeno))