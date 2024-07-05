from time import sleep

def main():
    a()
def a():
    print("a")
    sleep(1)
    b()
def b():
    print("b")
    sleep(1)
    c()
def c():
    print("c")
    sleep(1)
    main()


if __name__== "__main__":
    main()


