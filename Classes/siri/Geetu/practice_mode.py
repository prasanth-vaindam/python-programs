import random
import time
from collections import defaultdict
import os

MISTAKE_LOG = "mistakes_log.txt"
SLOW_LOG = "slow_responses_log.txt"
PRACTICE_LOG = "practice_log.txt"


def get_weak_tables(player_name):
    weak_tables = defaultdict(int)

    def extract_table(line):
        try:
            return int(line.strip().split("Table")[1].split(")")[0].strip())
        except:
            return None

    for filename in [MISTAKE_LOG, SLOW_LOG]:
        if os.path.exists(filename):
            with open(filename) as f:
                for line in f:
                    if player_name.lower() in line.lower():
                        table = extract_table(line)
                        if table:
                            weak_tables[table] += 1
    return sorted(weak_tables.items(), key=lambda x: -x[1])  # most frequent first


def play_practice_mode():
    print("🧠 Welcome to Practice Mode!")

    player_name = input("Enter your name: ").strip()
    weak_tables = get_weak_tables(player_name)
    print(f"🔍 Found {len(weak_tables)} weak table(s) based on your history.")
    if not player_name:
        print("❗ Please enter a valid name to start practicing.")
        return

    if not weak_tables:
        print("🎉 No weak tables found! You're doing great!")
        return

    print("\n📋 Your weak tables are:")
    for table, count in weak_tables:
        print(f" - Table {table} (appeared {count} times)")

    num_questions = 5
    print(f"\n🎯 You’ll get {num_questions} practice questions from your weak tables.")
    print("Let's begin!")
    print("-" * 50)

    stars = 0
    question_times = []
    total_start = time.time()

    for i in range(1, num_questions + 1):
        table = random.choice([t[0] for t in weak_tables])
        b = random.randint(1, 12)
        correct_answer = table * b

        print(f"\n🧩 Q{i}: What is {table} × {b}?")
        start_time = time.time()
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            user_answer = None
        end_time = time.time()

        time_taken = round(end_time - start_time, 2)
        question_times.append(time_taken)

        if user_answer == correct_answer:
            print(f"✅ Correct! ⭐ (Time: {time_taken}s)")
            stars += 1
        else:
            print(f"❌ Incorrect. Correct answer is {correct_answer} (Time: {time_taken}s)")

    total_time = round(time.time() - total_start, 2)

    print("\n" + "=" * 50)
    print(f"🏁 Practice Over! {player_name}, you got {stars}/{num_questions} correct.")
    print(f"🕒 Time Taken: {total_time}s")
    print("🧠 Stay consistent and you'll master them all!")

    with open(PRACTICE_LOG, "a") as f:
        f.write(f"{player_name},{stars}/{num_questions},{total_time}s, Tables: {[t[0] for t in weak_tables]}\n")

    print("📁 Practice session saved.\n")


# Run practice mode
play_practice_mode()
