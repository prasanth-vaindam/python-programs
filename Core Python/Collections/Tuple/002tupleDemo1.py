"""
If Python detects the same immutable object being reused,
it may point to the same memory (thanks to interning), but the
tuple still maintains separate slots for each index.

# Reassigning 'a' will not change the tuple, but it will change the list
"""

# tuple_obj = (1, 2, 3, 1, [1, 2, 3], [1, 2, 3], "apple", "apple")

# tuple_obj[6] = "orange"  # This will raise a TypeError because tuples are immutable

a = [1, 2, 3]

tuple_obj2 = (1, a, 2, a)
list_obj = [1, a, 2, a]
print(tuple_obj2)
print(list_obj)
a.append(4)  # Modifying the list 'a' will affect the tuple since it holds a reference to the list
# a = [1, 2, 3, 4]  # Reassigning 'a' does not change the tuple
print(tuple_obj2)  # The tuple still holds the original list reference
print(list_obj)  # The list will reflect the change in 'a' if it was mutable
print(list_obj)

