"""
Print the below pattern for n = 5
54321
5432
543
54
5
"""

n = int(input("enter n value: "))
for i in range(0, n):
    for j in range(0, n-i):
        print(n-j, end=" ")
    print()

