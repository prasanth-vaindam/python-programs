def factorial(n):
    if n == 1 or n == 0:
        return 1

    return factorial(n-2) * factorial(n-1)


print(factorial(5))