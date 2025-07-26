class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return None
        # return f"{self.name} is {self.age} years old"
        # print(f"{self.name} age is {self.age}")

p1 = Person("John", 36)
# print(str(None))  # when this is not producing error
print(str(p1))  # why this line is throwing error why can't it just print None
# print(p1)  # This will call the __str__ method implicitly
# x = p1.__str__()  # This will print the string representation of the object
# print(f"--> {x}")
# Uncommenting the __str__ method will allow it to be called implicitly