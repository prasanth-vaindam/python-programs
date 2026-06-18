sen = "python programming"

count = 0
for letter in sen:
    if letter.lower() in "aeiou":
        count += 1

print(f"There are {count} vowels in String '{sen}'")