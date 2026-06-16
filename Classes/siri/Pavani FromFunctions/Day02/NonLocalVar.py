x = 10

def outer():
    count = 0
    def inner():
        nonlocal count
        count = count + 1
        print("count in inner:", count)
        print(len("Hello"))

    inner()
    print("Outer:", x)


def fun():
    print("fun:", x)


# fun()
outer()