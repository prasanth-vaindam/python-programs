scores = {}

while True:
    player_name = input("enter name: ")
    score = int(input("enter score: "))

    previousScore = scores.get(player_name, 0)

    if score > previousScore:
        scores[player_name] = score

    stop = input("enter q or Q to quit")
    if stop.lower() == "q":
        break


print(scores)

# print the highest score in the list of players


