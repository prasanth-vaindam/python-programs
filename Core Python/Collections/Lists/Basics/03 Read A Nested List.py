n = eval(input("nested list: "))

print(n)
print(type(n))

for i in n:
    for j in i:
        print(j, end=" ")
    print()