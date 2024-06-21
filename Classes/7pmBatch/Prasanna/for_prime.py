def is_prime(x):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
        return True


n = int(input("enter a number: "))

if is_prime(n):
    print(n, "is a prime number")
else:
    print(n, "is not a prime a number")












