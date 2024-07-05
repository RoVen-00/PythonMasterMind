numero = int(input("numero a multiplicar: "))

for n in range(1, 11):
    if n % 2 == 0:
        print("{} x {} = {}".format(n, numero, n* numero))