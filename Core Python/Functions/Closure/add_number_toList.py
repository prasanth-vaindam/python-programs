def add_numbers_to_list(n):
    numbers = []
    numbers.append(n)
    print(numbers)

add_numbers_to_list(1)
add_numbers_to_list(2)
add_numbers_to_list(3)

def outer():
    numbers = []
    def inner(n):
        numbers.append(n)
        print(numbers)
    return inner


get_numbers = outer()

get_numbers(10)
get_numbers(20)
get_numbers(30)



