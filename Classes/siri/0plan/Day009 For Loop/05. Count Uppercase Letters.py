sen = "Python IS Awesome"

count = 0

for letter in sen:
    if letter.isupper():
        count +=1

print(f"There are {count} upper case letters")