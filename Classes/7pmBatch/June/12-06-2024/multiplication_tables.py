def multiplication_table(n):
    for i in range (1,11):
        print(f"{n} * {i}={n*i}" )
number=int(input("enter a number greater than zero to print the multiplicative table "))
multiplication_table(number)

