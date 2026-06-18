numbers = [10,20,3,4,6]

largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number

print(f"the largest number is {largest}")
