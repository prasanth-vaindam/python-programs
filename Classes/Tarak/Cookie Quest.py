# Cookie Quest
import random

# Table of 5 questions
questions = [
    (2, 5),
    (4, 5),
    (6, 5),
    (10, 5)
]

# Story parts
rewards = [
    "Mittens gets a warm cookie! 🍪",
    "Mittens finds a chocolate chip cookie! 🍪",
    "The leaf floats away, and Mittens gets another cookie! 🍪",
    "Mittens enters the Cookie Castle and finds a Giant Cookie Cake! 🎂🍪"
]

# Introduction
print("🐱 Welcome, Tarak! Let's help Mittens the Cat find cookies!")
print("To open each door, answer the table question correctly.\n")

# Game loop
for i, (num1, num2) in enumerate(questions):
    print(f"🚪 Door {i + 1}: What is {num1} x {num2}?")

    try:
        answer = int(input("👉 Your answer: "))
        if answer == num1 * num2:
            print("✅ Correct! 🎉", rewards[i])
        else:
            print("❌ Oops! That’s not cor   rect. Let's try again!")
            while True:
                try_again = int(input(f"🔁 Try again: What is {num1} x {num2}? "))
                if try_again == num1 * num2:
                    print("✅ Correct! 🎉", rewards[i])
                    break
                else:
                    print("❌ Not yet, try again!")
    except ValueError:
        print("⚠️ Please enter a number!")

    print("-" * 40)

# Ending
print("🏁 Tarak helped Mittens collect all the cookies! You’re awesome! 🐾")
