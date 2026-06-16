def outer():
    n = 0
    def inner():
        nonlocal n
        n +=1
        print(n)
    return inner

counter = outer()
counter()
counter()
counter()