nestedList = [[1, 2, 3], [4, 5], [6, 7], [8, 9, 10]]
print(nestedList)
finalList = []
for sublist in nestedList:
    for number in sublist:
        finalList.append(number)
print(finalList)

