def increment_key(i):
    i = i + 1
    return i


keys = ('a', 'b', 'c', 'd')
i = 1
generatedDict = dict.fromkeys(keys, increment_key(i))

print(generatedDict)
