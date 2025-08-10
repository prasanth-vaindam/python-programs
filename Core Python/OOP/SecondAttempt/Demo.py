class Person:
    # empty class can't be declared
    pass


p = Person()

print(p)  # None

print(type(p))  #

# --------------------------------------------------------------------

class Car:
    def __init__(self, a, b, samcharam=2020):
        self.regNo = a
        self.model = b
        self.year = samcharam
        self.milage = 10  # Default mileage
        self.ac = True  # Default air conditioning status

    def start(self):
        print(f"{self.year} {self.regNo} {self.model} is starting.")

    def stop(self):
        print(f"{self.year} {self.regNo} {self.model} is stopping.")

    def display_info(self):
        print(f"Car Info: {self.year} {self.regNo} {self.model}")

x = 10  # built in
abhilashCar = Car(4098, 2)  # we are creating a car object (which is user defined type), by calling it's constructor


print("milage of abhi car: ", abhilashCar.milage)
c2 = Car(3087,33)

#
# print(c)
# print(type(c))