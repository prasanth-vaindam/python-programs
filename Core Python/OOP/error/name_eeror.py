# if __main__ == "__main__":  # Wrong!
#     print("Running!")

# Correct way to check if the script is being run directly
if __name__ == "__main__":  # Correct!
    print("Running!")


class Car:
    def __init__(self, brand):
        self.brand = brand


my_car = Car("Toyota")
print(type(my_car))  # Output: <class '__main__.Car'>

# __main__.Car means:
# The Car class is defined in the main module, which is the current script being executed.
# The Car class is defined in the current file (my_car.py), not imported from somewhere else.
