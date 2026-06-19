num = int(input("Enter a number: "))

total = 0

while num > 0:
    digit = num % 10
    total += digit
    num //= 10

print("Sum =", total)