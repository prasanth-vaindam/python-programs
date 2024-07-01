thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
print(thisset)
# thisset.update(tropical)
thisset.union(tropical)

print("-> After Union",thisset) 

for x in thisset:
    print(x)

print("--> not ok",thisset.discard("banana1"))
print(thisset)
print("--> ok: ",thisset.discard("banana"))
# del thisset
print("After del:",thisset)
print("--> Before CLear",thisset)
thisset.clear()
print("--> After CLear",thisset)

# print("Poped Item:",thisset.pop())
