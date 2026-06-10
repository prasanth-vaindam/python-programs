def greet():
    print("Hello")

print(greet)

say_hello = greet

print(say_hello)
say_hello()

def execute(func):
    func()

execute(greet)