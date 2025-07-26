thisset = {"apple", "banana", "cherry"}
fruitsList = list(thisset)
print(type(fruitsList))
# Convert to a set if not already
# fruitsList.popItem("banana")  # popItem is not a valid method in Python sets
# thisset.popItem("banana")  # popItem is not a valid method in Python sets
# thisset.remove("banana")
# print(thisset)  # Uncomment to see the result after each operation
# thisset.discard("banana")  # discard does not raise an error if the element is not found

thisset.pop()  # pop removes a random element from the set
# thisset.clear()  # clear removes all elements from the set
# del thisset  # del removes the set completely
# print(thisset)  # Uncomment to see the result after each operation
print(thisset)