matrix = [[1, 2], [3, 4], [5, 6]]

print("row 2: ", matrix[1])

for row in matrix:
    print(row[0])
    pass

print("element", matrix[1][1])

# numbers_in_matrix = []
# for sublist in matrix:
#     for number in sublist:
#         numbers_in_matrix.append(number)




# How to do this with list comphrension
numbers_in_matrix = [x for sublist in matrix for x in sublist]

print(numbers_in_matrix)

# How to do this functional programming