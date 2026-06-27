"""
[[1, 4],
 [2, 5],
 [3, 6]]
"""
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix[1])

new_matrix = []

for i in  range(len(matrix[0])):
    for j in range(len(matrix[1])):
        if i == j:
            print(f"{matrix[0][i], matrix[1][j]}")


