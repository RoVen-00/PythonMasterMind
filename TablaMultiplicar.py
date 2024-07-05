
lista = [1, 2, 3, 4, 5, 6 ,7 ,8 ,9, 10]
numero_usuario = int(input("¿De que numero quieres la tabla de multiplicar?: \n"))
while numero_usuario not in lista:
    print("debe de estar entre el 1 y el 10")
    numero_usuario = int(input("¿De que numero quieres la tabla de multiplicar?: \n"))

for numero in lista:
        print(f"{numero_usuario} * {numero} = {numero_usuario*numero}") #la f en el print y combinado con los corchetes
        # y las variables hace que se puedan concatenar las strings con las variables
