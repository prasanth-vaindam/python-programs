"""
What is List?
A list is a collection which is ordered, changeable, and allows duplicate elements.
"""

names = ['Ravi', 'Hari', "o", 'Girl', 'One']

print(names[-1])  # One
# Accessing using +ve and -ve indexes
# print last 3 elements in nums list in all possible ways

# print(nums[-5:-1:-1])  # 1 -- unexpected []
nums = [1, 2, 0, 3, 4, 5]
print(nums[1:5:-1])  # 2 1 (or) we are getting empty []
print("13-> ", nums[-5:-1:-1])  # actual output is [] and we expected the elements at index -5 and -6 are printed i.e, 2 1
print(nums[-5:-1])  # 2 0 3 4
print(nums[0:-3])  # here it is considering the -3 in the rever direction and giving result

print(nums[-1:-5:-1])  # 4 3 0 2  (or) 5 4 3 0
print(nums[0:-3:-1])  # 1 5 4 (or) []
print(nums[0:-3:1])  # 1 2 0
print(nums[-1::])  # 5  what is the step value here?
# slicing
print("14--> ", nums[:])   # 1 2 0 3 4 5
print("15-->", nums[0:4:1])   # 1 2 0 3
print(nums[0:-3])  # empty list [] | [1,2,0]
print(nums[-5:-1])  # 2 0 3 4
print(nums[-5:-1:-1])  # 1 -- unexpected []
print(nums[-5:-1:1])  # 2 0 3 4
print("-->", nums[2:0:1])  # -->
print(nums[::2])  # 1 0 4
print(nums[:-1])  # 1 2 0 3 4
print(nums[-1:-3:1])  # 5 4 | 0 | []
print(nums[::])  # 1 2 0 3 4 5
print(nums[:-2:])  # 1 2 0 3
print(nums[-1::])  # 5  what is the step value here?
print("meaning less -->", nums[1:4:-1])  #
print(nums[-1:-5:-1])  # 4 3 0 2  ' 5 4 3 0
print(nums[::1])  # 1 2 0 3 4 5
print(nums[::-1])  # 5 4 3 0 2 1



# Modifying Lists
names[2] = "om"

# Add or Remove elements from list
names.append("a")
names.append(["a", "b"])
# how to add(append) multiple items into a list at once
# two ways: 1. to the original list  2. create a new list

my_list = [1, 2, 3]
new_items = [4, 5, 6]
# my_list.extend(new_items)
print(my_list)

# list(names, ..., names)
print(names)


