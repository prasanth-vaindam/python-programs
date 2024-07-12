# Write a python program to check if a number is even or odd

number = int(input("Enter number: "))

print("reminder: ", number % 2)
# Check if the number is divisible by 2
if number % 2 == 0:
    print(" number is even.")
else:
    print(" number is odd.")
