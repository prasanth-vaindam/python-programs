class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        return f"{self.year} {self.make} {self.model} is starting."

    def stop(self):
        return f"{self.year} {self.make} {self.model} is stopping."

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


class Car(Vehicle):

    def __init__(self):

    def Car(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def display_info(self):
        return f"Car Info: {self.year} {self.make} {self.model}, Doors: {self.doors}"