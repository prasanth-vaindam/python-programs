def f(name, age=18, *args, **kwargs):
    print(f"Name: {name}, Age: {age}")
    if args:
        print("Additional positional arguments:", args)
    if kwargs:
        print("Additional keyword arguments:", kwargs)
# Example calls to the function
f("Alice", 25, "Engineer", "New York", city="Los Angeles", hobby="Photography")
f("Bob", 30, city="San Francisco", hobby="Cycling")
f("Charlie", 22, "Student", "Boston")
f("David")  # Using default age
f("Eve", 28, "Designer", city="Chicago", hobby="Painting")