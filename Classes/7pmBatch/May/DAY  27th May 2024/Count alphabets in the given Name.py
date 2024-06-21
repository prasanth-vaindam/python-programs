# Write Python 3 code in this online editor and run it.
name = input('enter your name: ')
count = 0
for i in name:
    if i != ' ':
        count = count + 1
    else:
        continue

print("length of the name is: ", count)