from collections import defaultdict
import json


def generate_report(logs):
    total_questions = len(logs)
    correct_answers = sum(1 for log in logs if log["is_correct"])
    incorrect_answers = sum(1 for log in logs if not log["is_correct"] and not log["skipped"])
    skipped_questions = sum(1 for log in logs if log["skipped"])
    total_attempted = total_questions - skipped_questions
    average_time = round(sum(log["response_time_sec"] for log in logs) / total_questions, 2)

    table_stats = defaultdict(lambda: {"correct": 0, "total": 0})

    for log in logs:
        table = log["table"]
        table_stats[table]["total"] += 1
        if log["is_correct"]:
            table_stats[table]["correct"] += 1

    # Identify easiest and toughest tables
    table_accuracies = {
        table: round((data["correct"] / data["total"]) * 100, 1)
        for table, data in table_stats.items()
    }

    sorted_tables = sorted(table_accuracies.items(), key=lambda x: x[1])
    weakest_tables = sorted_tables[:3]
    strongest_tables = sorted_tables[-3:]

    # Print Report
    print("\n📊 Performance Report")
    print("-" * 30)
    print(f"Total Questions:     {total_questions}")
    print(f"Correct Answers:     {correct_answers}")
    print(f"Skipped Questions:   {skipped_questions}")
    print(f"Accuracy:            {round((correct_answers / total_questions) * 100, 1)}%")
    print(f"Average Time:        {average_time} sec/question")
    print("\n📉 Weakest Tables:")
    for t, acc in weakest_tables:
        print(f" - Table {t}: {acc}%")
    print("\n🏆 Strongest Tables:")
    for t, acc in strongest_tables:
        print(f" - Table {t}: {acc}%")

    return {
        "total_questions": total_questions,
        "correct_answers": correct_answers,
        "skipped_questions": skipped_questions,
        "accuracy": round((correct_answers / total_questions) * 100, 1),
        "average_time": average_time,
        "weakest_tables": weakest_tables,
        "strongest_tables": strongest_tables
    }


# Read JSON file
with open('prasanth_attempts.json', 'r') as file:
    logs = json.load(file)  # Converts JSON to a Python dictionary


print("-->", logs)
# Load from previous part
report = generate_report(logs)
