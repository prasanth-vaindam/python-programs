import time
from datetime import datetime
import json
import os
import uuid  # For generating unique session IDs
import random

def load_all_attempt_logs(filepath='all_players_attempts.json'):
    """Safely load previous logs from a file."""
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            print("⚠️ Warning: Could not read existing log file. Starting fresh.")
    return []

def save_all_attempt_logs(all_logs, filepath='all_players_attempts.json'):
    """Save all logs back to file."""
    with open(filepath, 'w') as f:
        json.dump(all_logs, f, indent=2)

def practice_mode(player_name="Kali"):
    """Practice multiplication tables, return list of logs with session ID."""
    questions = []
    logs = []
    session_id = str(uuid.uuid4())  # Unique session ID

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

        if answer == "":
            skipped = True
            is_correct = False
            given_answer = None
        else:
            skipped = False
            given_answer = int(answer) if answer.isdigit() else answer
            is_correct = (given_answer == correct_answer)

        logs.append({
            "session_id": session_id,
            "player_name": player_name,
            "question_id": question_id,
            "question": question_str,
            "given_answer": given_answer,
            "correct_answer": correct_answer,
            "is_correct": is_correct,
            "response_time_sec": response_time,
            "timestamp": timestamp,
            "skipped": skipped,
            "table": table
        })

    print(f"\n✅ Practice session completed for {player_name}!\n")
    return logs

# --- Run the session ---

player_name = input("Enter your name: ")
current_logs = practice_mode(player_name)

# Save player-specific session
with open(f"{player_name}_attempts.json", "w") as f:
    json.dump(current_logs, f, indent=2)
print(f"📁 Your session has been saved to {player_name}_attempts.json")

# Update and save to global attempts log
all_attempt_logs = load_all_attempt_logs()
all_attempt_logs.extend(current_logs)  # Add current logs
save_all_attempt_logs(all_attempt_logs)

print("📈 All player attempt logs updated successfully.")
