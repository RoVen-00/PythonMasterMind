import random
def string_mas_larga():
    lista_palabras = input("Ingresa las palabras separadas por espacios: ").split()
    if not lista_palabras:
        print("No se proporcionaron palabras.")
        return None
    resultado = max(lista_palabras, key=len)
    print("La palabra más larga es: {}".format(resultado))
    return resultado

# Definición de otras funciones (puedes agregar más funciones aquí)

def sumado_de_la_lista():
    lista_numeros = [int(x) for x in input("Ingresa los números separados por espacios: ").split()]
    resultado = 0
    for numero in lista_numeros:
        resultado += numero
    print("La suma de los números es: {}".format(resultado))
    return resultado

def par_inpar():
    numero = int(input("Ingresa un número: "))
    if numero % 2 != 0:
        print("El número {} es impar.".format(numero))
        return True
    else:
        print("El número {} no es impar.".format(numero))
        return False

def pregunta_algo():
    respuesta = input("¿Estás seguro? (responde 's' para sí, 'n' para no): ")
    if respuesta.lower() == 's':
        print("El usuario está seguro.")
        return True
    else:
        print("El usuario no está seguro.")
        return False

def convierte_a_mayus():
    cadena = input("Ingresa una cadena: ")
    cadena_mayus = ""
    for char in cadena:
        if 'a' <= char <= 'z':
            # Convertir el caracter a mayúscula sumándole la diferencia entre 'a' y 'A'
            char = chr(ord(char) - ord('a') + ord('A'))
        cadena_mayus += char
    print("Palabra en mayúsculas: {}".format(cadena_mayus))
    return cadena_mayus

def adivina_el_numero():
    numero_a_adivinar = random.randint(1, 100)
    while True:
        intento = int(input("Adivina el número (entre 1 y 100): "))
        if intento == numero_a_adivinar:
            print("¡Felicitaciones! Adivinaste el número.")
            break
        elif intento < numero_a_adivinar:
            print("El número es mayor. Intenta nuevamente.")
        else:
            print("El número es menor. Intenta nuevamente.")

def agregar_item_lista():
    lista_compra = ["pan", "leche", "huevos", "arroz"]
    while True:
        nuevo_item = input("Ingresa un nuevo ítem para la lista de la compra (o 'salir' para terminar): ")
        if nuevo_item.lower() == 'salir':
            break
        elif nuevo_item in lista_compra:
            print("El ítem '{}' ya existe en la lista.".format(nuevo_item))
        else:
            lista_compra.append(nuevo_item)
            print("El ítem '{}' ha sido agregado a la lista de la compra.".format(nuevo_item))
            print("Lista de la compra final:", lista_compra)


def main():

    string_mas_larga()
    sumado_de_la_lista()
    par_inpar()
    pregunta_algo()
    convierte_a_mayus()
    adivina_el_numero()
    agregar_item_lista()



if __name__ == "__main__":
    main()