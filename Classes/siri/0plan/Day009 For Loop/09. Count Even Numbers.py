numbers = [10,4,5,6,7,8]
count = 0
for number in numbers:
    if number%2==0:
        count += 1

print(f"the number of even numbers in the list are {count}")