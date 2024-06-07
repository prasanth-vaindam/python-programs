n = int(input("Enter n"))
res = 1
while n>1:
    res *= n
    n -= 1

print(res)

def factorial(n):
    t = n
    fact = 1
    for i in (1, t+1):
        fact *= i
    return fact


res = factorial(5)
print(res)
