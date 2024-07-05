def medir_largos(palabra, *args, sumar_todo=False):

    if args:
        largos = [len(palabra)]
        for a in args:
            largos.append(len(a))
        if sumar_todo:
            largos = sum(largos)
        return largos
    return len(palabra)

def main():
    print(medir_largos("rico"))
    print(medir_largos("sabroso", "delicioso", "estupendo", sumar_todo=True))

if __name__ == "__main__":
    main()