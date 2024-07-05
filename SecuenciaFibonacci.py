def fibonacci_recursivo(n):
    if n <= 1:
        return 1
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

#La secuiencia de fibonacci es el resultado de la suma de un numero con su anterior: 1+1= 2, 2+1= 3 3+2=5 5+4=8...
#Basicamente dado un numero en la funcion main ( range(10) ) si el numero es igual o menor que uno devuelve 1. Si no, devuelve la suma 10-1 mas 10-2.
# Como hemos llamado a la funcion con un for y 10 es un rango, hasta que no se de la condicion del if va a seguir sumando los numeros.

def main():
    for a in range(10):
        print(fibonacci_recursivo(a))

if __name__ == "__main__":
    main()