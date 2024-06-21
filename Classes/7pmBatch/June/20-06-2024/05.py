# Cartesian Product
# Compute the Cartesian product of two lists.
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
cartesian_product = [(x, y) for x in list1 for y in list2]
print(cartesian_product)
