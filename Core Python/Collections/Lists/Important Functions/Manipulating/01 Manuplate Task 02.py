# add all the numbers divisible by 10 in the range of 100 list
n = list(range(101))
total = 0
for i in n:
    if i % 10 == 0:
        total += i

print(total)
