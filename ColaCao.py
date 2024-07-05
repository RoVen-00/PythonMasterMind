print("voy a la cocina")
print("miro si hay leche")

hay_leche = input("¿hay leche? (s/n)")
hay_colacao = input("¿Hay colacao? (s/n)")

if hay_leche != "s" or hay_colacao != "s":
    print("voy a comprar al super...")
    if hay_leche != "s":
        print("compro leche")
    if hay_colacao != "s":
        print("compro colacao")

print("ponemos la leche en el vaso")
print("ponemos el colacao en el vaso")
print("mezclamos")