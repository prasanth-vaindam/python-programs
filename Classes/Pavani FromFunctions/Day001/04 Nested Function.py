def outer():
    x = 1000
    def inner():
        x = 2000
        print(x)
    inner()
    print(x)

outer()