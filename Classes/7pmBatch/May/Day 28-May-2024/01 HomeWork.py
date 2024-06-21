# Write a python program to print the squares of all the even numbers present in a given list of numbers.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = eval(input("enter a list of numbers: "))
for i in numbers:
    if i % 2 == 0:
        print("square of", i, " is", i*i)
        print(f"square of {i} is {i*i}")
