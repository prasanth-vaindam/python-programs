import matplotlib.pyplot as plt
from collections import defaultdict
import os

MISTAKE_LOG = "mistakes_log.txt"
SLOW_LOG = "slow_responses_log.txt"


def read_mistakes(player_name=None):
    table_errors = defaultdict(int)
    if os.path.exists(MISTAKE_LOG):
        with open(MISTAKE_LOG) as f:
            for line in f:
                if "Table" in line and (player_name is None or player_name.lower() in line.lower()):
                    try:
                        table = int(line.strip().split("Table")[1].strip().replace(")", ""))
                        table_errors[table] += 1
                    except:
                        continue
    return table_errors


def read_slow_responses(player_name=None):
    slow_counts = defaultdict(int)
    if os.path.exists(SLOW_LOG):
        with open(SLOW_LOG) as f:
            for line in f:
                if "Table" in line and (player_name is None or player_name.lower() in line.lower()):
                    try:
                        table = int(line.strip().split("Table")[1].split(")")[0].strip())
                        slow_counts[table] += 1
                    except:
                        continue
    return slow_counts


def plot_bar_chart(data, title, filename, color):
    if not data:
        print(f"⚠️ No data to plot for {title}")
        return
    tables = list(data.keys())
    values = list(data.values())

    plt.rcParams['font.family'] = 'Segoe UI Emoji'  # or NotoColorEmoji on Linux
    plt.figure(figsize=(10, 6))
    bars = plt.bar(tables, values, color=color)
    plt.xlabel("Table Number")
    plt.ylabel("Count")
    plt.title(title)
    plt.xticks(tables)
    plt.grid(True, linestyle="--", alpha=0.3)

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2 - 0.2, height + 0.1, f"{int(height)}")


    plt.tight_layout()
    plt.savefig(filename)
    print(f"📊 Saved chart: {filename}")
    plt.close()


def generate_charts():
    print("📈 Generating Table Performance Charts...")
    plt.rcParams['font.family'] = 'Segoe UI Emoji'  # or NotoColorEmoji on Linux
    mistakes = read_mistakes()
    slow_responses = read_slow_responses()

    plot_bar_chart(
        mistakes,
        title="❌ Tables with Most Mistakes",
        filename="table_mistakes_chart.png",
        color="tomato"
    )

    plot_bar_chart(
        slow_responses,
        title="🐢 Tables with Slowest Answers",
        filename="slow_responses_chart.png",
        color="orange"
    )


# Run the chart generator
generate_charts()
