text = input("Enter a string: ")

i = 0
count = 0

while i < len(text):
    if text[i].lower() in "aeiou":
        count += 1
    i += 1

print("Vowels:", count)