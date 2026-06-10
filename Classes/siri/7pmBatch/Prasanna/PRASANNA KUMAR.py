# program  to count the alphabets in a given name

name = str(input("enter a name: "))

count = 0

for i in name:
    if i != ' ':
        count = count + 1
    else:
        continue

print("length of the name is",count)
