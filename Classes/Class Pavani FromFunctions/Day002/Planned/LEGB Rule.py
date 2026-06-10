x = 100

def outer():
    x = 200

    def inner():
        x = 300

        print("Local:", x)
        print("Built-in:", len("Python"))

    inner()

outer()