import random


def play_math_game():
    print("🎮 Welcome to Geetu’s Math Quest!")
    print("✨ Answer the questions and earn stars! ⭐")
    print("-" * 50)

    stars = 0
    num_questions = 12

    for i in range(1, num_questions + 1):
        a = random.randint(1, 12)
        b = random.randint(1, 12)
        correct_answer = a * b

        print(f"🚪 Door {i}: What is {a} × {b}?")
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
                print("✅ Correct! You earned a ⭐\n")
                stars += 1
            else:
                print(f"❌ Oops! The correct answer was {correct_answer}.\n")
        except ValueError:
            print("⚠️ Please enter a number.\n")

    print("=" * 50)
    print(f"🏆 Game Over! You earned {stars} out of {num_questions} stars.")
    if stars == num_questions:
        print("🌟 Perfect! You're a Math Hero, Geetu!")
    elif stars >= 5:
        print("🎉 Great job! Keep practicing and you'll reach the stars!")
    else:
        print("💪 Good effort! Let’s try again tomorrow and get more stars!")


# Start the game
play_math_game()
