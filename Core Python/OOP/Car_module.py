class Car:
    def __init__(self, a, b, samcharam):
        self.brand = a
        self.model = b
        self.year = samcharam
        self.milage = 10  # Default mileage

    def start(self):
        print(f"{self.year} {self.brand} {self.model} is starting.")

    def stop(self):
        print(f"{self.year} {self.brand} {self.model} is stopping.")

    def display_info(self):
        print(f"Car Info: {self.year} {self.brand} {self.model}")


# car = Car()  # here I am calling the Car class constructor


# print(car)
# print(type(car))

# car_one = Car("Toyota", "Corolla", 2020)
# car_two = Car("Honda", "Civic", 2021)