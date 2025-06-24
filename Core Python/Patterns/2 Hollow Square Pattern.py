
"""
* * * * *
*       *
*       *
*       *
* * * * *

"""
def hollow_square_pattern(size):
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


hollow_square_pattern(5)