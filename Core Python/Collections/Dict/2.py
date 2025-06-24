# Create a Dictionary


# Animals = {"name": "Cow"}
# print(type(Persons))
# print(type(Animals))

Persons = {}
while True:
    name = input("enter name: ")
    age = int(input("age: "))

    # Persons[name] = age

    Persons[name] = Persons.get(name,)
    stop = input("Press 'Q' or 'q'  to stop entering values into Persons ")
    if stop.lower() == 'q':
        break

# to print the values in the Persons dictionary
print(Persons)



# Cars = dict([("name","TaTa"), ("name","Ferrari")])
# Persons.update("name":name, "age":age)
