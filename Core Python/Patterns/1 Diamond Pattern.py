"""
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

"""
def diamond_pattern(rows):
    for i in range(rows):
        print(" " * (rows - i - 1) + "*" * (2 * i + 1))
    for i in range(rows - 2, -1, -1):
        print(" " * (rows - i - 1) + "*" * (2 * i + 1))


diamond_pattern(5)