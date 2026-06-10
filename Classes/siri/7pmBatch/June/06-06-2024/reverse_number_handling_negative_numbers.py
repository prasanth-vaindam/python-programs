# Program to reverse a given number

def reverse_number(number, sign):
    temp = number
    rev = 0     # variable to store the reversed number
    while temp > 0:
        rev = rev * 10 + temp % 10
        temp //= 10

    print(f"The reverse of the given number {number} is {sign}{rev}")


while True:
    number = int(input("Enter a number: "))
    if number < 0:
        reverse_number(abs(number), "-") # abs() is built in function to make negative numbers positive numbers
    else:
        reverse_number(number,"")
