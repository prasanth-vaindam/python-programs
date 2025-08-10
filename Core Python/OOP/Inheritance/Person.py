class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


# Use the Person class to create an object, and then execute the printname method:
#
# x = Person("John", "Doe")
# x.printname()

class Student(Person):
    pass
    # def __init__(self, fname, lname, year):
    #     super().__init__(fname, lname)
    #     self.graduationyear = year
    #
    # def welcome(self):
    #     print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# Now the Student class has the same properties and methods as the Person class.
# However, we can add new properties and methods to the Student class.
# ravi = Student("Ravi", "Kumar", 2023)
ravi = Student("Ravi", "Kumar")
# ravi.welcome()
ravi.printname()