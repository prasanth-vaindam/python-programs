word = "TOY"

reverse = "".join(reversed(word))

# print(reverse)

# traversing an iterable

iterator = reversed(word)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
x = 1
if x == 1:

    print("---")

else:
    print("No")

for i in range(5):
    if i == 2:
        pass  # do nothing, just skip this cycle
    print("Pass:", i)
print("-------------start------------")
for i in range(5):
    if i == 3:
        pass  # just skip doing anything
    else:
        print(i)
    print("->", i)
print("-------------stop------------")


while True:
    pass

print("Hi")










