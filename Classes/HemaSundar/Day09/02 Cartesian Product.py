"""
[('Red', 'S'),
 ('Red', 'M'),
 ('Red', 'L'),
 ('Blue', 'S'),
 ('Blue', 'M'),
 ('Blue', 'L')]
"""

colors = ["Red", "Blue"]
sizes = ["S", "M", "L"]
# for i in colors:
#     for j in sizes:
#         print(f"({i},{j})")

new_list = [ (i,j) for i in colors for j in sizes]
print(new_list)
for i in new_list:
    print(i)

