# Write a python program to check if a number is even or odd

number = int(input("Enter number: "))
# Check if the number is divisible by 2
if number // 2 * 2 == number:
    print(" number is even.")
else:
    print(" number is odd.")
