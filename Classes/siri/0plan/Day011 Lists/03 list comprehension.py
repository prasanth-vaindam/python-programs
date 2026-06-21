# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
fruits = ['apple', 'banana', 'orange','kiwi','mango']

sublist = [x for x in fruits if 'a' in x]
print(sublist)