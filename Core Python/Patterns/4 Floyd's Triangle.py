"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

"""
def floyds_triangle(rows):
    num = 1
    for i in range(rows):
        for j in range(i + 1):
            print(num, end=" ")
            num += 1
        print()


floyds_triangle(5)