b=int(input("Que numero quieres multimplicar: "))
for a in range(1, 11):
    if a % 2 == 0:
        print("{} x {} = {}".format(a,b,a*b))
