numeros_introducidos = input("introduzca los numeros separados por comas y espacios: ")
numeros_de_usuario = numeros_introducidos.split(", ")
numeros_de_usuario_limpios = []

for numero in numeros_de_usuario:
    numeros_de_usuario_limpios.append(int(numero))

print("El numero mas grande es el {} y el numero mas pequeño es el {}".format(max(numeros_de_usuario_limpios), min(numeros_de_usuario_limpios)))