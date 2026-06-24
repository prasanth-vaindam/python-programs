

"""
Print the below pattern for n = 4

4321
432
43
4

"""

n = int(input("enter n value: "))
for i in range(1, n+1):
    for j in range(0, n+1-i):
        print(n-j, end=" ")
    print()

