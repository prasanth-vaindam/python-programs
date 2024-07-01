
"""
Print the below pattern for n = 4

****
***
**
*

"""

n = int(input("enter n value: "))
for i in range(1, n+1):
    for j in range(1, n+2-i):
        print("*", end=" ")
    print()

