

"""
Print the below pattern for n = 4

1
12
123
1234

"""

n = int(input("enter n value: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

