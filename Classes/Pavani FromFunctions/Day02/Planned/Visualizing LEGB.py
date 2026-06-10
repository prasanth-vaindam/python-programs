x = "Global"

def outer():
    x = "Enclosing"

    def inner():
        x = "Local"

        print(x)          # Local
        print(len("Hi"))  # Built-in

    inner()

outer()