def div(x,y):
    return x/y

def smart_div(func):
    def wrapper(x,y):
        if x < y:
            x, y = y, x
            return func(x,y)
    return wrapper


div = smart_div(div)

print(div(10,2))
print(div(2,10))

