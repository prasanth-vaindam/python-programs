# Program to reverse a given number

def reverse_number(number):
    temp = number
    rev = 0     # variable to store the reversed number
    while temp > 0:
        rev = rev * 10 + temp % 10
        temp //= 10
    print(f"The reverse of the given number {number} is {rev}")


while True:
    reverse_number(int(input("Enter a number: ")))