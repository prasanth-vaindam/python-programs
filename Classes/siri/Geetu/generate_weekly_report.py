from collections import defaultdict
import os

SCORES_FILE = "scores.txt"
MISTAKE_LOG = "mistakes_log.txt"
SLOW_LOG = "slow_responses_log.txt"


def read_mistakes(player_name=None):
    table_errors = defaultdict(int)
    if os.path.exists(MISTAKE_LOG):
        with open(MISTAKE_LOG) as f:
            for line in f:
                if "Table" in line and (player_name is None or player_name.lower() in line.lower()):
                    table = int(line.strip().split("Table")[1].strip().replace(")", ""))
                    table_errors[table] += 1
    return table_errors


def read_slow_responses(player_name=None):
    slow_counts = defaultdict(int)
    if os.path.exists(SLOW_LOG):
        with open(SLOW_LOG) as f:
            for line in f:
                if "Table" in line and (player_name is None or player_name.lower() in line.lower()):
                    table = int(line.strip().split("Table")[1].split(")")[0].strip())
                    slow_counts[table] += 1
    return slow_counts


def read_player_scores(player_name=None):
    player_stats = defaultdict(lambda: {"games": 0, "total_stars": 0, "total_time": 0.0})
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE) as f:
            for line in f:
                name, stars, total_time = line.strip().split(",")
                if player_name is None or player_name.lower() == name.lower():
                    stars = int(stars)
                    total_time = float(total_time)
                    player_stats[name]["games"] += 1
                    player_stats[name]["total_stars"] += stars
                    player_stats[name]["total_time"] += total_time
    return player_stats


def generate_report(player_name=None):
    print("📊 WEEKLY MATH TABLE REPORT")
    print("=" * 40)

    # Part 1 – Tables Most Missed
    mistakes = read_mistakes(player_name)
    if mistakes:
        print("\n❌ Tables Most Missed:")
        for table, count in sorted(mistakes.items(), key=lambda x: -x[1]):
            print(f"Table {table}: {count} mistakes")
    else:
        print("\n✅ No mistakes logged this week!")
        print("\n✅ No mistakes logged" + (f" for {player_name}" if player_name else "") + "!")

    # Part 2 – Tables Most Slow
    slow_tables = read_slow_responses(player_name)
    if slow_tables:
        print("\n🐢 Tables Answered Slowly:")
        for table, count in sorted(slow_tables.items(), key=lambda x: -x[1]):
            print(f"Table {table}: {count} slow responses")
    else:
        print("\n🚀 No slow responses logged this week!")
        print("\n🚀 No slow responses logged" + (f" for {player_name}" if player_name else "") + "!")

    # Part 3 – Player Performance Summary
    stats = read_player_scores(player_name)
    if stats:
        print("\n👤 Player Performance:")
        print(f"{'Player':<12} {'Games':<6} {'Avg Stars':<10} {'Avg Time (s)':<12}")
        for player, data in stats.items():
            avg_stars = data["total_stars"] / data["games"]
            avg_time = data["total_time"] / data["games"]
            print(f"{player:<12} {data['games']:<6} {avg_stars:<10.2f} {avg_time:<12.2f}")
    else:
        print("\n📁 No player scores yet!")


# 👇 Run full report (all players)
# generate_report()

# 👇 OR run user-specific report
# generate_report("gitesh")

player_name = input("Enter player name (leave blank for all): ").strip()
generate_report(player_name if player_name else None)
