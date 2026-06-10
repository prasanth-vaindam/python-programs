def multiplier(n):
    def multiply(x):
        return n*x
    return multiply

double = multiplier(2)
print(double(10))