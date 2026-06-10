# type casting

var_float = 123.78
print(f"value is {var_float} and its type is {type(var_float)}")
var_int = int(var_float)  # explicit type casting 
print(f"value is {var_int} and its type is {type(var_int)}")

# # implict type conversion
# a = 10
# b = 23.98
# c = a + b # implicit type conversion
# print("c's type: ",type(c))

a = 10
b = 3
print("16-->",type(a//b), " ", a//b)

# # String to int
str_var = "123"
print("20->",int(str_var))

# # String to Float
str_var = "123.45"
print("24-->",int(123.45))
print("24-->",int(str_var))
print("-->", float(str_var))

# String to Decimal - wrong use case
str_var = "ten"
print("-->",int(str_var))

