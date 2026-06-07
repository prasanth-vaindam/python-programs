# numbers = []
# def add_numbers(n):
#     numbers.append(n)
#     print(numbers)
#
#
# add_numbers(10)
# add_numbers(20)
# add_numbers(30)

def outer():
    numbers = []
    def inner(number):
        numbers.append(number)
        print(numbers)
    return inner

get_numbers = outer()
get_numbers(1)
get_numbers(2)
get_numbers(3)

