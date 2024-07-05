def potencia(numero, exponente=2):
    resultado = numero
    for a in range(1, exponente):
        resultado *= numero
    return resultado

#Dado un numero calcular su potencia. 1ª siendo su exponente 2
#                                     2ª con un exponente a elegir

#nuestra potencia se compone te un numero y un exponente
#por cada numero del 1 al exponente multiplica la base por si misma.
# es decir multiplica el 4 por si mismo 5 veces.
def main():
    print(potencia(4))
    print(potencia(4, 5))

if __name__ == "__main__":
    main()

