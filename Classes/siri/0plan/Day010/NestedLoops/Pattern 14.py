"""
Print the below pattern for n = 5
enter n: 5

        1
      1 0 1
    1 0 1 0 1
  1 0 1 0 1 0 1

Process finished with exit code 0

"""

n = int(input("enter n: "))

for i in range(0, n):
    for l in range(0,n-i):
        print(" ", end=" ")
    for j in range(1, (2*i)):
        print(int(j % 2), end =" ")
    print()
