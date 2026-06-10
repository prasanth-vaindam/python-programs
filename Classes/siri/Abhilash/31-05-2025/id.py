a = 10
b = 10
c = 20

print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))

a = 100
print("---------------------")
print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))
