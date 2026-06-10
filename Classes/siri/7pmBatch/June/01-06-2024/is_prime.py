# Program to Check if the given number is prime or not
import math

def is_prime(n):
    if n < 0:
        # print("It is a Negative Number, Please enter a Positive number!")
        return False
    if n == 0 or n == 1:
        # print("It is not neither Prime nor Composite")
        return False

    if n == 2:
        # print("2 is a Even Prime Number")
        return True

    for i in range(2, int(math.sqrt(n))+1):
        if n % i != 0:
            continue
        else:
            # print(f"The given  number {n} is not a Prime Number")
            return False

    # print(f"The Given number is {n} is a  Prime Number")
    return True

# while True:
#     is_prime(int(input("enter a number to check if it is a prime : ")))


# Program to print all the prime numbers between 1 to n
list_of_prime_numbers_up_to_n = []

while True:
    n = int(input("Enter a N value up to where you need to print the prime numbers: "))

    list_of_prime_numbers_up_to_n = []

    for i in range(1, n+1):
        if is_prime(i):
            list_of_prime_numbers_up_to_n.append(i)

    print(list_of_prime_numbers_up_to_n)


# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97