# Program to find the gcd of two numbers
def gcd(n1, n2):
    while n2 > 0:
        rem = n2 % n1
        if rem == 0:
            return n1
        else:
            n2 = n1

    return gcd()