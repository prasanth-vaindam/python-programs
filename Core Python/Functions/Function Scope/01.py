def outer():

    count = 0

    def inner():

        nonlocal count

        count += 1

        print(count)

    return inner

counter = outer()

counter()
counter()
counter()