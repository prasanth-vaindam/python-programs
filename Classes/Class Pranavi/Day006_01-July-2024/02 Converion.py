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
# str_var = "123"
# print("20->",int(str_var))

# # String to Float
# str_var = "123.45"
# print(float(str_var))

# String to Decimal - wrong use case
str_var = "ten"
# print("-->",int(str_var))

# Bool Type - Boolean values or Truth Values : {True and False}
i = 1
print("i = 1 ->",bool(i))
i = 10
print("i = 10 ->",bool(i))
i = 10.5
print("i = 10.5 ->",bool(i))
i = 0.345
print("i = 0.345 ->",bool(i))
i = 0
print("i = 0 ->",bool(i))
i = 0.0
print("i = 0.0 ->",bool(i))
i = 0 + 1j
print("i = 0 + 1j ->",bool(i))
i = 0 + 0j
print("i = 0 + 0j ->",bool(i))
i = True
print("i = True ->",bool(i))
i = False
print("i = False ->",bool(i))
i = "Pranavi"
print('i="Pranavi', bool(i))
i = "O"
print('i="O"', bool(i)) 
i = ""
print('i=""', bool(i)) 



print("True + True is : ", True - False)



