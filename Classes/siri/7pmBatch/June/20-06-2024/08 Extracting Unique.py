# Extract unique elements from a list while preserving order.
lst = [1, 2, 2, 3, 4, 4, 5]
unique = []
[unique.append(x) for x in lst if x not in unique]
print(unique)
