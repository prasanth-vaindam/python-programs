x = 123  # int
y = 123.67  # float

new_y = int(y)

print(f"{y} is {type(y)}")
print(f"{new_y} is {type(new_y)}")
new_x = float(x)

print(f"5: {x} is {type(x)}")
print(f"6: {new_x} is {type(new_x)}")


print(f"{x} is now {float(x)}")
print(f"{y} is now {int(y)}")

z = "123.679"
# print(f"{z} is converted to int will be {int(z)} ")
print(f"{z} is converted to float will be {float(z)}")
