fact1 = 1
i = 1


def factorial(n, fact11, u) -> int:
    if u > n:
        # print(f"Factorial of {n} is {fact11}")
        return fact11
    else:
        fact11 = fact11 * u




factorial(1, 1, 1)

# x = int(input("enter a number:"))
answer = factorial(5, 1, 1)
print("from my call factorial(5, 1, 1) -->", answer)
# factorial(x, fact1, i)
# print(f"The factorial of {x} is {factorial(x, fact1, i)}")
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
# num = int(input("Enter number of terms: "))
#
# for i in range(num):
#     print(fibonacci(i), end=' ')
