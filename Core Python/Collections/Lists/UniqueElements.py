l1 = [1, 2, 4, 5, 66]
l2 = [1, 2, 45, 67, 40, 32]

print(l1, l2)

result = []
for element in l1:
    if element in l2:
        result.append(element)

print(result)
elements = list(set(list(l1 + l2)))
elements.sort()


print(f"unique elements after joining two lists{l1} and {l2} are {elements}")
