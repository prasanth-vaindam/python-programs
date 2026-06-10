import random


j = 10

for k in range(1, 12 ):
    i = random.randint(1, 10)
    ans = int(input(f"what is {j} * {i} ?: "))

    if j * i == ans:
        print("Correct!")
    else:
        print(f"The Correct answer is {j*i}")
