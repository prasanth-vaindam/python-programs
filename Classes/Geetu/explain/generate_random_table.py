# program to generate a random table
import random
def generate_random_table():
    """Generate a random multiplication table from 1 to 12."""
    table = random.randint(1, 12)
    return table


count = 0
while True:
    x = random.randint(1, 13)
    print(f" {count} : x is {x}")
    count += 1
    if count == 12:
        break
print(x)