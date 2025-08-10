class Car:
    miles = 0

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.milage = 0

    def display_info(self):
        print(f"{self.year} {self.make} {self.model} - Milage: {self.milage} miles")


c = Car("Toyota", "Corolla", 2020)
c.display_info()
c.milage = 15000
c.display_info()
Car.miles = 10000  # Setting class variable
c.miles = 5000
c.data = "This is a class variable or instance variable or object variable?"
print("c.data", c.data)  # Accessing instance variable
print("-->why is miles variable's value not shared among the two objects (or) all objects of this Car class", c.miles)  # Accessing class variable
print("---------------------------------------")
cab = Car("Honda", "Civic", 2019)
cab.display_info()
# print("cab.data", cab.data)  # Accessing instance variable
cab.milage = 20000
cab.display_info()
print("-->why is miles variable's value not shared among the two objects (or) all objects of this Car class", cab.miles)  # Accessing class variable
print("---------------------------------------")