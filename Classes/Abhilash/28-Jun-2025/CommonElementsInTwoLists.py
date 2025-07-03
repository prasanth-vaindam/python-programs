listOne = [6, 9, 2, 8, 0, 7, 7, 0]
listTwo = [7, 11, 2, 0, 4, 8]
newList = []

for i in listOne:
    for j in listTwo:
        if i == j and j not in newList:
            newList.append(i)

print(newList)


