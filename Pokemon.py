
from random import randint
import os

VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 90
#A parte de variables tenemos constantes, es lo mismo, contenedores que guardan algo
#la diferencia es que las constantes ni cambian en todo el programa ni se pueden modificar
#Ademas, se escriben todo en mayuscula para diferenciarlas

TAMANIO_BARRA_VIDA = 20

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE
#En este momento la vida de ambos es su vida inicial

while vida_pikachu > 0 and vida_squirtle > 0:

    print("turno de Pikachu")

    ataque_pikachu = randint(1,2)

    if ataque_pikachu == 1:
        print("Pikachu ataca con bola voltio")
        vida_squirtle -= 10
    else:
        print("Pikachu ataca con onda trueno")
        vida_squirtle -= 11




    barra_vida_pikachu = int(vida_pikachu * TAMANIO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
    print("Pikachu:    [{}{}] ({})/({})".format("*" * barra_vida_pikachu, " ",
                                                *(TAMANIO_BARRA_VIDA - barra_vida_pikachu,
                                                  vida_pikachu, VIDA_INICIAL_PIKACHU)))
    #Barra de vida de pikachu

    barra_vida_squirtle = int(vida_squirtle * TAMANIO_BARRA_VIDA / VIDA_INICIAL_SQUIRTLE)
    print("Squirtle:    [{}{}] ({})/({})".format("*" * barra_vida_squirtle, " ",
                                                 *(TAMANIO_BARRA_VIDA - barra_vida_squirtle,
                                                   vida_squirtle, VIDA_INICIAL_SQUIRTLE)))
    #barra de vida de squirtle




    input("enter para continuar...\n")
    os.system("cls")
    print("limpieza de pantalla (en PyCharm no funciona en CMD si)")
    print("turno Squirtle")

    ataque_squirtle = None

    while ataque_squirtle not in ["p", "a", "b", "n"]:
        ataque_squirtle = input('elige tu ataque [p]lacaje, [a]gua, [b]urbuja, [n]nada: \n\n')
    if ataque_squirtle == "p":
        print("Squirtle ataca con placaje")
        vida_pikachu -= 10
    elif ataque_squirtle == "a":
        print("Squirtle ataca con agua")
        vida_pikachu -= 12
    elif ataque_squirtle == "b":
        print("Squirtle ataca con burbuja")
        vida_pikachu -= 9
    elif ataque_squirtle == "n":
        print("no haces nada")


    if vida_pikachu < 0:
        vida_pikachu = 0

    if vida_squirtle < 0:
        vida_squirtle = 0

    barra_vida_pikachu = int(vida_pikachu * TAMANIO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
    print("Pikachu:    [{}{}] ({})/({})".format("*" * barra_vida_pikachu, " ",
                                                *(TAMANIO_BARRA_VIDA - barra_vida_pikachu,
                                                  vida_pikachu, VIDA_INICIAL_PIKACHU)))


    barra_vida_squirtle = int(vida_squirtle * TAMANIO_BARRA_VIDA / VIDA_INICIAL_SQUIRTLE)
    print("Squirtle:    [{}{}] ({})/({})".format("*" * barra_vida_squirtle, " ",
                                                 *(TAMANIO_BARRA_VIDA - barra_vida_squirtle,
                                                   vida_squirtle, VIDA_INICIAL_SQUIRTLE)))



if vida_pikachu > vida_squirtle:
    print("Pikachu gana!")
else:
    print("Squirtle gana!")
