# a python program to check if a given number is a prime number or not.
def is_prime(num):
    i = 1
    count = 0

    if x % i == 0:
        count = count + 1

    if count == 2:
        print(x," a prime number ")
    else:
        print("Not a prime number")


x = int(input("enter a number to check if it is prime: "))

is_prime(x)
# print(is_prime(x))

