print("-------------------------------")
i = 0
while i < 3:
    i += 1
    print(i)
print("-------------------------------")


# what does the range produce
for i in range(1, 6):
    print(i)

print("-------------------------------")
x = 0
while x < 3:
    print(x)
    x += 1

print("-------------------------------")
x = 5
if x > 10:
    print("A")
else:
    print("B")
print("-------------------------------")



if x := 0:
    print("ok")
elif not x:
    print("x is 0")
else:
    print("Finally")
# Question: which operator is used to check equality in conditionals
print("------------------------------")
if x == 5:
    print("True if x == 5")

print("------------------------------")

x = 7
if x < 10:
    print("Less than 10")
elif x < 20:
    print("Less than 20")

print("---------------------------")

