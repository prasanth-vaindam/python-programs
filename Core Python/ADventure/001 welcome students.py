# Welcome program that greets user and plays with their name

print("👋 Hello, let's do some Python magic!")
name = input("What is your name? ")

print(f"Welcome, {name.upper()}!")
print("Your name backwards is:", name[::-1])
print("Let's see how cool your name is...")

if len(name) > 6:
    print("Wow! Your name has real character! 🏆")
else:
    print("Short and sweet, just like good code! 💡")
