names = ['apple', 'amit', 'abhi', 'bob', 'boy', 'cat', 'dance', 'do']

d = {}
count = 0
temp_count = 0

for name in names:
    startingLetter = name[0]
    value = ""
    for tempName in names:
        if tempName.startswith(startingLetter):
            count += 1

    for temp_name in names:
        if temp_name.startswith(startingLetter):
            temp_count += 1
            if temp_count == count:
                value += temp_name
            else:
                value += temp_name + ","

    d[startingLetter] = value
    count = 0
    temp_count = 0

print(d)
