# Program to reverse a number

def reverse_number(number):
    temp = number
    print("In Function: ", temp)
    rem = 0
    while temp > 0:
        print("Temp >0", temp)
        rem = rem * 10 + temp % 10
        print("in loop rem", rem)
        temp //= 10
    print(f"The reverse of the given number {number} is :", rem)


while True:
    reverse_number(int(input("Enter a Number: ")))
