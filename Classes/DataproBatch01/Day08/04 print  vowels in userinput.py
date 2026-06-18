word = input("Enter Name: ")
count = 0
for letter in word:
    if letter in "aeiou":
        count = count + 1
        # print(letter)

print(f"the number of vowels in the given word {word} are {count}")