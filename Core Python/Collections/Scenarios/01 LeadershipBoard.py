scores = {}

while True:
    try:
        player_name = input("Enter player name: ").strip()
        if not player_name:  # Handle empty names
            print("Please enter a valid name")
            continue

        score = int(input("Enter score: "))

        previous_score = scores.get(player_name, 0)

        if score > previous_score:
            scores[player_name] = score
            print(f"New high score for {player_name}: {score}!")
        else:
            print(f"Score {score} doesn't beat {player_name}'s current high score of {previous_score}")

    except ValueError:
        print("Please enter a valid number for score")
        continue

    if input("Press 'q' to quit or any key to continue: ").lower() == 'q':
        break

print("\nFinal Leaderboard:")
for player, score in scores.items():
    print(f"{player}: {score}")