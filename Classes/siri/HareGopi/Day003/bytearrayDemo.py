ba = bytearray([65,66,67])

print(ba)
ba[0] = 70
print(ba)

# creating from string
ba2 = bytearray("Hello", "utf-8")
print(ba2)