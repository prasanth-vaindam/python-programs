names = ['apple', 'amit', 'bob', 'boy', 'cat', 'dance', 'do']

"""
1. Sort Alphabetically
count the number of items which beign with the same alphabet  
"""
d = {}
count = 0

for name in names:
    startingLetter = name[0]
    value = ""
    for iname in names:
        if iname.startswith(startingLetter):
            count += 1
            if count == 1:
                value = iname + ","
            else:
                value += iname

    d[startingLetter] = value
    count = 0

print(d)

    #
#
# result_dict = {name: name[0] for name in names}
# print(result_dict)
#
# # result_dict = {name[0]: name for name in names}
# # print(result_dict)
#
# # collect all the values which are same and concatenate the keys
#
# temp_dict = {}
# checkedAlphabets = []
# for alphabet in result_dict.values():
#     for k, v in result_dict.items():
#         if alphabet == v and alphabet not in checkedAlphabets:
#             # checkedAlphabets.append(alphabet)
#
#             temp_dict[alphabet] = temp_dict.get(alphabet, "") + k
#
# print("--->", temp_dict)
#
#
