name = input("Enter Full Name: ")

words = name.split()

for word in words:
    print(word[0], end="")