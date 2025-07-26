import time
from datetime import datetime
import json

# Practice Mode for Multiplication Tables

# This function allows a player to practice multiplication tables by answering questions.

def practice_mode(player_name="Kali"):
    import random

    questions = []
    logs = []  # ← List to store attempt logs

    print(f"\n🧠 Practice Mode for {player_name} — Answer or press Enter to skip.\n")

    for table in range(2, 13):
        for i in range(1, 11):
            questions.append((table, i))

    random.shuffle(questions)

    for table, multiplier in questions:
        correct_answer = table * multiplier
        question_str = f"{table} x {multiplier}"
        question_id = f"{table}x{multiplier}"

        start_time = time.time()
        answer = input(f"{question_str} = ").strip()
        response_time = round(time.time() - start_time, 2)
        timestamp = datetime.now().isoformat(timespec='seconds')

        # Determine correctness or skip
        if answer == "":
            skipped = True
            is_correct = False
            given_answer = None
        else:
            skipped = False
            given_answer = int(answer) if answer.isdigit() else answer
            is_correct = (given_answer == correct_answer)

        # Log this attempt
        attempt_log = {
            "question_id": question_id,
            "player_name": player_name,
            "question": question_str,
            "given_answer": given_answer,
            "correct_answer": correct_answer,
            "is_correct": is_correct,
            "response_time_sec": response_time,
            "timestamp": timestamp,
            "skipped": skipped,
            "table": table
        }

        logs.append(attempt_log)

    print(f"\n✅ Practice session completed for {player_name}!\n")

    return logs  # You can later save this to file or analyze it


# Example usage
# This is a simple practice mode for multiplication tables.
# This function can be called to start the practice mode for a player.
player_name = input("Enter your name: ")
current_attempt_logs = practice_mode(player_name)
# Optional: Save logs to file
with open(f"{player_name}_attempts.json", "w") as f:
    json.dump(current_attempt_logs, f, indent=2)
print(f"Your practice attempts have been saved to {player_name}_attempts.json")

# Store logs form this session in the global file where all stats are stored, will this be
with open('all_players_attempts.json', 'r') as file:
    # List to store all attempt logs
    all_attempt_logs = json.load(file)  # Converts JSON to a Python dictionary


# Append current session logs to the global list
all_attempt_logs.append(current_attempt_logs)

with open(f"all_players_attempts.json", "w") as f:
    json.dump(all_attempt_logs, f, indent=2)

