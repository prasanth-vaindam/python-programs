def add(x, y): return x + y


def sub(x, y): return x - y


def mul(x, y): return x * y


def div(x, y): return x / y if y != 0 else "Cannot divide by zero"


print("Options: +, -, *, /")
op = input("Choose operation: ")
a = float(input("First number: "))
b = float(input("Second number: "))

if op == "+":
    print("Result:", add(a, b))
elif op == "-":
    print("Result:", sub(a, b))
elif op == "*":
    print("Result:", mul(a, b))
elif op == "/":
    print("Result:", div(a, b))
else:
    print("Unknown operation")
