a = 1  # class int
b = 10.09  # class float
c = 1 + 8j  # class complex
is_raining = False  # class bool
name = "Ganesh!"  # class str

future_var = None  # NoneType
# -----------------------------
#  Basic Data Types in Python
# They are immutable - the literals cannot be changed in place

print(name[0])  # G
print(len(name))  # 7
print(name)  #

print(name[6]) # !

# print(name[len(name)])  # error

print("Indexes Demo")
print(name[0], " ", name[-7]) # G G
print(name[1], " ", name[-6]) # a a
print(name[2], " ", name[-5])  # n n
print(name[3], " ", name[-4])  # e e
print(name[4], " ", name[-3])  # s s
print(name[5], " ", name[-2])  # h h
print(name[6], " ", name[-1])  # ! !
# --------- immutable means they can't be changed in place
# name[6] = "."
name = "lion is the king"
# name = "Ganesh!"
print(name[0: -3])  #

