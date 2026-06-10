# program to demonstrate break: Count the number of letters with in the given string present before the space character

name = input('enter your name: ')
count = 0
for i in name:
    if i == ' ':
        break
    else:
        count += 1

print("length of the name is: ", count)
