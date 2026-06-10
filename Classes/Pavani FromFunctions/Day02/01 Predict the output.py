x = 100

def outer():
    x = 200

    def inner():
        x = 300
        print("Inner:", x)

    inner()
    print("Outer:", x)

outer()
print("Global:", x)