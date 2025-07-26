n = int(input("enter a number of fibonacci series:"))

a = 0
b = 1
print("0 1", end=" ")
for i in range(0, n):
    next_element = a + b
    print(next_element, end=" ")
    a = b
    b = next_element
