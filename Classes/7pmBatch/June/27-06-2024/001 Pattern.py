# program to print the below pattern when n = 4

n = int(input("enter a number: "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()