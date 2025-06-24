"""
The Gaming Leaderboard
You're building a mobile game where players submit their high scores. You need to store player names with their best scores, and quickly look up any player's current high score to see if their new score beats it.
What data structure would you use and why?
"""

scores = {
    "name": "Prasanth",
    "currentScore": 900
}
print(scores)
keys_list = scores.keys()
values_list = scores.values()

# what happens in the below line?
requriedKey = keys_list.__getstate__()

# how do you insert values into dictionary
# how to compare a value you get from dictionary

while True:
    name = input("Enter Name")
    currentScore = int(input("Enter your Score: "))

    previousScore = scores.get(name)
    if previousScore >= currentScore:
        pass
    else:
        scores.update({name: currentScore})

    print(scores)

    if x := input("Enter Q to quit entering data: ") == "Q":
        break

# print("2", scores)


