from time import sleep
def medir_largos(palabra, *args):
    """
    def sumar_numeros(num1, num2):
        return num1 + num2
    print(sumar_numeros(12, 23))
    """

    if args:
        largos = [len(palabra)]
        for a in args:
            largos.append(len(a))
        return largos
    return len(palabra)

def main():
    print(medir_largos("rico"))
    print(medir_largos("sabroso", "delicioso", "estupendo"))

if __name__ == "__main__":
    main()