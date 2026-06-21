"""
Program 2: Convert Temperature from Celsius to Fahrenheit

Question:
Write a Python program to accept the temperature in Celsius from the user,
convert it to a floating-point number, calculate the Fahrenheit temperature,
and display the result.

Formula

F = (C × 9/5) + 32
"""
# Accept temperature
celsius = float(input("Enter temperature in Celsius: "))

# Convert
fahrenheit = (celsius * 9 / 5) + 32

# Display
print("\nTemperature in Fahrenheit:", fahrenheit)