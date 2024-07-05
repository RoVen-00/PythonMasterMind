vocales = "aeiou"
frase = "Hola, hoy estoy aprendiendo Python"
vocales_encontradas = 0

for letra in frase:
    if letra in vocales:
        print("He encontrado una {}".format(letra))
        vocales_encontradas += 1

print("El numero de vocales_encontradas es: {}".format(vocales_encontradas))