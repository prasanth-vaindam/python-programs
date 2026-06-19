numbers = [15, 42, 8, 67, 25]

i = 0
largest = numbers[0]

while i < len(numbers):
    if numbers[i] > largest:
        largest = numbers[i]
    i += 1

print("Largest:", largest)