

"""
Print the below pattern for n = 4

1
22
333
4444

"""

n = int(input("enter n value: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(i, end=" ")
    print()
