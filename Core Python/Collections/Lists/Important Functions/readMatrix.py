rowSize = int(input("enter number of rows: "))
columnSize = int(input("enter number of columns: "))

matrix = []

tempRow = []
for i in range(rowSize):
    for j in range(columnSize):
        # tempRow.clear()
        tempRow.append(int(input(f"enter element of {i, j}")))

    print("length", len(tempRow), "\n tempRow", tempRow)
    matrix.append(tempRow)
    print("matrix in j loop: ", matrix)

print(matrix)