x = "Good"  # global variable
carname = "volvo"

def fun():
    global  x
    x = "Awesome" # local variable
    print(x)


fun() # function call

print(x)
print('Hello', 'World')