x = 100 # x is global variable
def fun():
    print("Inside Function fun()",x)

fun()
print("value of x is ", x)