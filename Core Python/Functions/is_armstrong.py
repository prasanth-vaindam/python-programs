# Program to check if the given number is an armstrong number

def is_armstrong(number):
    no_of_digits = len(str(number))
    original_number = number
    armstrong_sum = 0
    while number > 0:
        t = number % 10
        armstrong_sum = armstrong_sum + pow(t, no_of_digits)
        number //= 10
    if armstrong_sum == original_number:
        # print(f"Yes, the given number {original_number} is Armstrong number\n")
        return True
    else:
        # print("Not an armstrong number")
        return False


list_of_armstrong_numbers = []
for i in range(1, 5000000):
    if is_armstrong(i):
        list_of_armstrong_numbers.append(i)

print(list_of_armstrong_numbers)