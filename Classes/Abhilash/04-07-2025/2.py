temp_dict = {'q': [3, ['b', 'c', 'c']], 'w': [4, ['c', 'c', 'c', 'c']], 'e': [1, ['c']]}

sorted_dict = sorted(temp_dict.items(), key=lambda item: item[1][0], reverse=True)

print(sorted_dict)

for student in sorted_dict:
    if student[1][0] > 1:
        print(f"{student[0]} has the following skills -> {student[1][1]}")

# print(sorted_dict)
# print()
