respuesta = None

while respuesta != "a" and respuesta != "b" and respuesta != "c":
    respuesta = input("que opcion prefieres? [a, b, c]")

if respuesta == "a":
    print("has elegido bien")
elif respuesta == "b":
    print("podrias haber elegido mejor")
elif respuesta == "c":
    print("elegiste mal")
else:
    print("no tiene sentido")
