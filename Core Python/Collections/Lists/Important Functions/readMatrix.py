rowSize = int(input("enter number of rows: "))
columnSize = int(input("enter number of columns: "))

matrix = []
tempRow = []  # here it gets already in each iteration
for i in range(rowSize):
    # tempRow = []  # here it gets already in each iteration
    for j in range(columnSize):
        tempRow.append(int(input(f"enter element of {i, j}")))
    print(f"Intermediate:  {tempRow}")
    # matrix += list(tempRow)
    matrix.append(list(tempRow))
    tempRow.clear()
    # matrix.append(tempRow)

print(matrix)

