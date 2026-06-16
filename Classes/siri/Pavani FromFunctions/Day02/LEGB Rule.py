x = 10

def outer():

    def inner():
        print("inner:", x)
        print(len("Hello"))

    inner()
    print("Outer:", x)


def fun():
    print("fun:", x)


# fun()
outer()