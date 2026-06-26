nums = [1,3,4,5,6]
nums.insert(1,2)
print(nums)

list_two = [4,5,6]

nums.extend(list_two)
print(nums)

fruits = ['apple', 'banana']
more_fruits = ['cherry', 'orange']

fruits.extend(more_fruits)

l = fruits + nums
print("---->",l)
print(fruits)

# print(nums.pop(4))
nums.remove(4)
print(nums)
# list_two.remove("two")
# print(list_two)

# del list_two
# print(list_two)

list_two.clear()
print(list_two)