sen = "Python is awesome learn python"
word = input("Enter key value to search:....")

if word in sen:
    print(f"the word {word} is present in the sentence \n ' {sen} '")
else:
    print(f"the word {word} is not present")


a = 10
b = 20

print(f"the sum of {a} and {b} is {a+b}")