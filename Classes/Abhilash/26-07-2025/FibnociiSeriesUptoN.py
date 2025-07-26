n = int(input("Enter the value of N: "))


def fibonacci_upto_n(n):
    fib_series = []
    a, b = 0, 1
    while a <= n:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series


print("Fibonacci series up to", n, "is:", fibonacci_upto_n(n))
