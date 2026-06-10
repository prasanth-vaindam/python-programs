# Original dictionary
temp_dict = {'q': [3, ['b', 'c', 'c']], 'w': [4, ['c', 'c', 'c', 'c']], 'e': [1, ['c']]}

# Step 1: Convert values to a list
values_list = list(temp_dict.values())


# Step 2: Define a function to use as a sort key
def get_sort_key(item):
    return item


# Step 3: Sort using the function
sorted_list = sorted(values_list, key=get_sort_key)

# Step 4: Print the result
print(sorted_list)
