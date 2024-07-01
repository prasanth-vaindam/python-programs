a = 1  # class int
b = 10.09  # class float
c = 1 + 8j  # class complex
is_raining = False  # bool
name = "Ganesh!"  # string
future_var = None  # NoneType
# -----------------------------
#  Basic Data Types in Python
# They are immutable - the literals cannot be changed in place

print(name[0])  # G
print(len(name))  #
print(name)  #

print(name[6])
print(name[len(name) - 1])  #
# print(name[len(name)])  # error - out of range

print("Indexes Demo")
print(name[0], " ", name[-7])
print(name[1], " ", name[-6])
print(name[2], " ", name[-5])
print(name[3], " ", name[-4])
print(name[4], " ", name[-3])
print(name[5], " ", name[-2])
print(name[6], " ", name[-1])
# --------- immutable means they can't be changed in place
# name[6] = "."

