# Identity operators compare whether
# two variables refer to the same object in memory,
# not whether their values are equal.

list1 = [10, 20, 30]
list2 = list1

print(list1 is list2)

# Both list1 and list2 refer to the same list.