x = 10
def outer():
    x = 20
    def inner():
        global x
        x +=1

    inner()
    print(x)

outer()