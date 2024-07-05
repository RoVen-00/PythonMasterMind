import string
texto_del_usuario = input("introduzca un texto: ")
letras_mayusculas = 0

for letra in texto_del_usuario:
    if letra in string.ascii_uppercase:
        letras_mayusculas += 1

print("Las mayusculas son {}".format(letras_mayusculas))