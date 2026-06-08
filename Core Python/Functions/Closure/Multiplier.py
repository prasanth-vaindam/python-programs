def multiplier(n):
    def multiply(x):
        return n*x
    return multiply


double = multiplier(2)
print(double(10))
triple = multiplier(3)
print(triple(10))
fourth = multiplier(4)
print(fourth(10))