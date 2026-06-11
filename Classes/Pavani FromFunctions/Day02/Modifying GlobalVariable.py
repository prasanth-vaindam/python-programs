x = 10
def outer():
    x = 20
    def inner():
        global x
        print("inner:",x)
    inner()
    print("Outer:",x)

def fun():
    print("fun:",x)



fun()
outer()