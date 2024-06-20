print("Hello")
try:
    print(10/9)
except ValueError:
    print("Value error")
except ZeroDivisionError:
    print("Division by Zero not allowed")
else:
    print("Else")


print("Hello outside")
