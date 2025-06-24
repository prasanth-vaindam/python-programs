Persons = {}

name = input("enter name: ")
age = int(input("Enter age: "))

Persons[name] = Persons.get(name, age)

print(Persons)

# how to update the age
name = input("enter name: ")
age = int(input("Enter age: "))

currentAge = Persons.get(name,0)
if age > currentAge:
    Persons[name] = age

# Persons[name] = Persons.get(name, Persons.get(name)>age:Persons.get(name))
print(Persons)