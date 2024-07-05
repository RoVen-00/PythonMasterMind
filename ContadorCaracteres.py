#Esto es un programa derivado de la parte de las listas del curso de nate, pero es personal, no es un ejercicio suyo.
import string
vocal = ["a", "e", "i", "o", "u"]
consonante = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "ñ", "p",\
               "q", "r", "s", "t", "v", "w", "x", "y", "z"]
espacio= " "
cantidad_vocales=0
cantidad_consonantes=0
cantidad_espacios=0
cantidad_otros_caracteres=0
cantidad_letras_mayusculas=0

empezar_denuevo = input("pulsa a para empezar\n")
while empezar_denuevo == "a":
    frase = input("Escribe una frase: ")#lower() aqui te convierte el imput a minusculas, pero como ahora
    # queremos que las cuente lo que hacemos es añadir import string y el bloque de la linea 24,25 y 26
    for letra in frase:
        if letra in vocal:
             cantidad_vocales+=1
        elif letra in espacio:
            cantidad_espacios+=1
        elif letra in consonante:
            cantidad_consonantes+=1
        else:
            cantidad_otros_caracteres+=1
    for letra in frase:
        if letra in string.ascii_uppercase:
            cantidad_letras_mayusculas+=1
    print("la cantidad de vocales en {} es {}\n\
    La cantidad de consonantes es {}\n\
    La cantidad de espacios es {}\n\
    La cantidad de otros caracteres es {}\n\
    La cantidad de mayusculas es {}".format(frase, cantidad_vocales, cantidad_consonantes, cantidad_espacios,\
                                            cantidad_otros_caracteres, cantidad_letras_mayusculas))

    for letra in frase:
        if letra in vocal:
            print("He encontrado una {}".format(letra))
        elif letra in consonante:
            print("He encontrado una {}".format(letra))

else:
    print("Te largas por gracioso")
