"""
Print the below pattern for n = 5
54321
4321
321
21
1
"""

n = int(input("enter n value: "))
# for i in range(0, n):
#     count = n-i
#
#     while count >= 1:
#         print(count, end=" ")
#         count -= 1
#     print()

for i in range(0, n):
    for j in range(n-i, 0, -1):
        print(j, end=" ")
    print()
