word = input("Enter a word: ")

alphabetCount = 0


for i in word:
    if i.isalpha():
        alphabetCount += 1

print("number of alphabets in given word", alphabetCount)
