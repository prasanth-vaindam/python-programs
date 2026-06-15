number = int(input("Enter the Number: "))
print(number % 2 == 0)
is_even = number % 2 == 0
if not is_even:
    print("Odd Number!")
else:
    print("Even Number!")