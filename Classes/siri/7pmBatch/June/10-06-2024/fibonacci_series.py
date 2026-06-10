def fibonacci_series_up_to_n(n):
    fib_series = [0,1]
    a = 0
    b = 1
    while len(fib_series) < n:
        fib_series.append(a+b)
        temp = b
        b = a + b
        a = temp
    return fib_series


while True:
    print(fibonacci_series_up_to_n(int(input("Enter a number greater than 2:"))))