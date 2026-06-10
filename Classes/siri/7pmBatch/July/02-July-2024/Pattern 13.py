"""
Print the below pattern for n = 5
1
1 0 1
1 0 1 0 1
1 0 1 0 1 0 1
"""

n = int(input("enter n: "))

for i in range(0, n):
    for j in range(0, (2*i-1)):
        print(int(j % 2), end=" ")
    print()
