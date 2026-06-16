def multiplier(n):
    def multiply(x):
        return n*x
    return multiply

double = multiplier(2)

triple = multiplier(3)
print(double(10))
print(triple(10))