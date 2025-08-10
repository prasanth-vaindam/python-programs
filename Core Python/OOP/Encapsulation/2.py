class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius


    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15°C is not possible!")
        self.__celsius = value

    @property
    def fahrenheit(self):
        return (self.__celsius * 9/5) + 32


# Example usage:
temp = Temperature(-425)
print(temp.celsius)     # ✅ Access like an attribute
print(temp.fahrenheit)  # ✅ Computed property

temp.celsius = 100      # ✅ Uses setter internally
temp.celsius = -300   # ❌ Raises ValueError
