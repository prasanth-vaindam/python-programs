# # Unpacking
# list123 = [[2, 3, 9], [2, 8, 5, 7], [5, 6, 7]]
# i, j, k = list123
#
# print(i)  # [2, 3, 9]
# print(j)  # [2, 8, 5, 7]
# print(k)  # [5, 6, 7]
#
# studentInfo = ["Abhilash", "ICFAI College",  "Hyderabad", "24STUCHH010639", 18]
# name, college_name, city, rollNumber, age = studentInfo
#
# print(f"{name} is {age} years old studying in {college_name}")
#
# # packing
# persons = name, "Ganesh", "ravi"
#
# print(persons)
#
x = 1
y = 2
print(f"Values of x, y before swapping is {x, y}")

# x = x + y
# y = x - y
# x = x - y

not_tuple_containing_two_numbers = [y, x]
print("28-->", not_tuple_containing_two_numbers)
# x, y = not_tuple_containing_two_numbers
x, y = [100, 200]

print(f"Values of x, y after swapping is {[x, y]}, {y}")