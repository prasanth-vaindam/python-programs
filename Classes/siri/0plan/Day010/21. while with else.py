numbers = [10, 20, 30, 40, 50]

i = 0

while i < len(numbers):
    if numbers[i] == 100:
        print("Number found!")
        break
    i += 1
else:
    print("Number not found.")