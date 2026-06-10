import random
import time
import os

SCORES_FILE = "scores.txt"
MISTAKE_LOG = "mistakes_log.txt"

def play_math_game():
    print("🎮 Welcome to Geetu’s Math Quest!")
    player_name = input("Enter your name: ").strip()
    print(f"Hi {player_name}! Let's begin your math challenge.")
    print("-" * 50)

    stars = 0
    num_questions = 8
    question_times = []
    asked_questions = set()  # to avoid repeats

    total_start_time = time.time()

    for i in range(1, num_questions + 1):
        # Ensure unique question
        while True:
            a = random.randint(1, 12)
            b = random.randint(1, 12)
            question = (a, b)
            if question not in asked_questions:
                asked_questions.add(question)
                break

        correct_answer = a * b

        print(f"\n🚪 Door {i}: What is {a} × {b}?")
        start_time = time.time()
        try:
            user_answer = int(input("Your answer: "))
            end_time = time.time()
            time_taken = round(end_time - start_time, 2)
            question_times.append(time_taken)

            if user_answer == correct_answer:
                print(f"✅ Correct! You earned a ⭐ (Time taken: {time_taken}s)")
                stars += 1
            else:
                print(f"❌ Oops! The correct answer was {correct_answer}. (Time: {time_taken}s)")
                log_mistake(player_name, a, b, user_answer, correct_answer)
        except ValueError:
            end_time = time.time()
            time_taken = round(end_time - start_time, 2)
            question_times.append(time_taken)
            print("⚠️ Invalid input. No star for this one.")
            log_mistake(player_name, a, b, "Invalid", correct_answer)

    total_time = round(time.time() - total_start_time, 2)

    print("\n" + "=" * 50)
    print(f"🏁 Game Over! {player_name}, you earned {stars} out of {num_questions} stars.")
    print(f"🕒 Total Time Taken: {total_time} seconds")
    print("⭐ Individual Question Times:", question_times)

    # Save to file
    with open(SCORES_FILE, "a") as file:
        file.write(f"{player_name},{stars},{total_time}\n")

    print("📁 Your score has been saved!\n")
    show_leaderboard()


def log_mistake(player_name, a, b, user_answer, correct_answer):
    with open(MISTAKE_LOG, "a") as f:
        f.write(f"{player_name} missed: {a}×{b} = {a*b}, answered: {user_answer} (Table {a})\n")


def show_leaderboard():
    print("\n🏆 Leaderboard (Top Performers)")
    print("-" * 40)

    if not os.path.exists(SCORES_FILE):
        print("No scores yet. Be the first star!")
        return

    players = []
    with open(SCORES_FILE, "r") as file:
        for line in file:
            name, stars, time_taken = line.strip().split(",")
            players.append((name, int(stars), float(time_taken)))

    # Sort: first by stars (desc), then by time (asc)
    players.sort(key=lambda x: (-x[1], x[2]))

    print(f"{'Rank':<5} {'Name':<15} {'Stars':<6} {'Time (s)':<8}")
    for idx, (name, stars, t) in enumerate(players[:10], start=1):  # top 10
        print(f"{idx:<5} {name:<15} {stars:<6} {t:<8}")

# Run the game
play_math_game()
