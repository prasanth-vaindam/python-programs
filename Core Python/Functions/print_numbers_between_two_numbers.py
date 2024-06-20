# Program to print numbers between two numbers by checking the limits

m = int(input("Enter a First Number: "))
n = int(input("Enter another Number: "))

left_limit = 0
right_limit = 0

if m > n:
    right_limit = m
    left_limit = n
else:
    right_limit = n
    left_limit = m

while left_limit <= right_limit:
    print(left_limit)
    left_limit += 1
