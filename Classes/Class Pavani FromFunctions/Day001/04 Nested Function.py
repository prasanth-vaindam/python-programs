def outer():

    def inner():
        x = 2000
        print(x)
    inner()
    print(x)

outer()