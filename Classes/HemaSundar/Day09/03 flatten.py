numbers = [[1,2],[3,4],[4,5,6]]

# new_list = []
# for i in numbers:
#     for j in i:
#         new_list.append(j)
#
# print(new_list)

new_list = [j for i in numbers for j in i]
print(new_list)