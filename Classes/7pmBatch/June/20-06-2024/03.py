# Flatten a matrix (2D list) into a single list.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [element for row in matrix for element in row]
print(flattened)

# Filter a list of lists to include only even numbers.
filtered = [[element for element in row if element % 2 == 0] for row in matrix]
print(filtered)