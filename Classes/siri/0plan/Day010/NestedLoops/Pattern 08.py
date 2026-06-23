"""
Print the below pattern for n = 5

5
54
543
5432
54321

"""

n = int(input("enter n value: "))
for i in range(1, n+1):
    for j in range(0, i):
        print(n-j, end=" ")
    print()

