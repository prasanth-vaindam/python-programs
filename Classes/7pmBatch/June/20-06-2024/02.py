# Create a list of squares of even numbers and cubes of odd numbers.
numbers = list(range(1, 11))
result = [x**2 if x % 2 == 0 else x**3 for x in numbers]
print(result)
