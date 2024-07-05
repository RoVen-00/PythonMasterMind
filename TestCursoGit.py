from time import sleep
def sumar_uno(a):
    print(a)
    sleep(1)
    a += 1
    if a != 101:
        sumar_uno(a)

def main():
    sumar_uno(1)


if __name__ == "__main__":
    main()