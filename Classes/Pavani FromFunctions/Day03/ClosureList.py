def outer():
    numbers = []
    def inner(n):
        numbers.append(n)
        print(numbers)
    return inner

store_number = outer()
store_number(1)
store_number(10)
store_number(123)