# Even Number
# Odd Number
# Sum of Numbers
# Prime Number with For loop
# print the values in the tuple
# minimum and maximum
# length of tuple
# concatenation of tuples
# multiplying of tuple
# properties of tuple
# slicing in tuple

# differences between tuple and list : () [];  mutability;

this_list = [1]

print(type(this_list))
m = (1, 2, 3, 4, 5, 6, 7)
print(type(m))
print(" line 20: ", m[1:4])  # 2,3,4,5
print(m[1:])  # 2,3,4,5,6,7
print(m[1:len(m)])  # 2,3,4,5,6,7

this_list.append(2)
print(this_list)

print("-->", m[0])
m[0] = 33
# m.append(25)  # AttributeError: 'tuple' object has no attribute 'append'
