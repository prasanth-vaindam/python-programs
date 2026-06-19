text = input("Enter a string: ")
ch = input("Enter character: ")

i = 0
count = 0

while i < len(text):
    if text[i] == ch:
        count += 1
    i += 1

print("Occurrences:", count)