name = input("What is your name? ")
hour = int(input("What hour is it (0 to 23)? "))

if 5 <= hour < 12:
    greeting = "Good Morning"
elif 12 <= hour < 17:
    greeting = "Good Afternoon"
else:
    greeting = "Good Evening"

print(f"{greeting}, {name}! Let's have a great day of learning Python 🌞")
