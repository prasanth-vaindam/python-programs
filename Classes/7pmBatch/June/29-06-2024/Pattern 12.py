"""
Print the below pattern for n = 5
15 14 13 12 11
10 9 8 7
6 5 4
3 2
1
"""

n = int(input("enter n: "))
count = n * (n+1)//2

for i in range(1, n+1):
    for j in range(0, n-i+1):
        print(count, end=" ")
        count -= 1
    print()
