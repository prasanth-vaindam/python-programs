# program to check if the given number is a palindrome
# Method One Find the Reverse

inputNumber = int(input("Enter a number to check if it is palindrome: "))
n = inputNumber
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10;

if rev == inputNumber:
    print(f"Yes the given number {inputNumber} is a palindrome! ")
else:
    print(f"The given number {inputNumber} is not a palindrome! ")

