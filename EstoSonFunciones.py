"""def saludo_sectario(name):
    print("hola {}".format(name[::-1]))


saludo_sectario("nate")
saludo_sectario("sara")
saludo_sectario("dani")
"""
def largo_string(mi_string):
    largo = 0
    for letra in mi_string:
        largo += 1
    return largo

largo_de_la_string = largo_string("hola mundo")

print(largo_de_la_string)
