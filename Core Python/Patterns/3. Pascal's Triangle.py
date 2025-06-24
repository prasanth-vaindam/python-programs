"""
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
"""
def pascals_triangle(rows):
    for i in range(rows):
        row = [1]
        for j in range(1, i + 1):
            row.append(row[-1] * (i - j + 1) // j)
        print(" " * (rows - i - 1), end="")
        print(*row)


pascals_triangle(5)