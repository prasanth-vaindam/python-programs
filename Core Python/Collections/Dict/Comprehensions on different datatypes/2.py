from collections import defaultdict

names = ['apple', 'amit', 'abhi', 'bob', 'boy', 'cat', 'dance', 'do']
grouped = defaultdict(list)

print("1 --->", grouped)

for name in names:
    # grouped[name[0]].append(name)
    grouped[name[0]] = grouped.get(name[0], []) + [name]  # List merging
    print("in loop --->", grouped)

result = {letter: ",".join(names) for letter, names in grouped.items()}
print(result)
