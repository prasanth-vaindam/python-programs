x = 1
y = 1
# print(id(x))
# y = 2.4
z = "silence"


# print(x)
# print(hex(id(x)))
# print(id(y))

numbers = [1, 2, 3, 4, 5, 6]

numbers_duplicated = numbers
nums = numbers.copy()

# print(hex(id(numbers)))
# print(hex(id(numbers_duplicated)))
# print(hex(id(nums)))


numbers_duplicated[1] = "apple"
print(numbers_duplicated[1])
print(numbers)
print(nums)

nums[1] = "dog"
print(numbers)

print(nums)

print(numbers)
print(numbers_duplicated)
print(nums)


numbers[0] = "One"
print(numbers)
print(numbers_duplicated)
print(nums)


"""
shallow copy vs assigning object reference 

how deep copy is similar to listObject.copy()

https://labex.io/tutorials/python-how-to-understand-object-references-in-python-398254
two list when assigned to each other are same object references because they point to the same object in memory
"""