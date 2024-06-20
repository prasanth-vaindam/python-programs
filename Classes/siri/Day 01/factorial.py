n = int(input("Enter a number: "))
factorial = 1
temp = n
while temp >=1:
    factorial = factorial*temp
    temp = temp - 1
print(factorial)