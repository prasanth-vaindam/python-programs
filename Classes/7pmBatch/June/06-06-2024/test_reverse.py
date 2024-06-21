def reverse_number(number):
    if number == 0:
        print("The reverse of the given number is 0")
        return

    temp = abs(number)
    rev = 0     # variable to store the reversed number
    while temp > 0:
        rev = rev * 10 + temp % 10
        temp //= 10

    if number < 0:
        print(f"The reverse of the given number {number} is -{rev}")
    else:
        print(f"The reverse of the given number {number} is {rev}")


while True:
    number = int(input("Enter a number: "))
    reverse_number(number)
