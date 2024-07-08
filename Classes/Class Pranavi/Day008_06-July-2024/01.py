# Note: Python is Dynamically Typed 
# Strong Typed - Java C C++ are strongly typed, which means variable type cannot be changed once decalred
x = "Namaste World"  
x = 20 
x = 20.5
x = 1j 
x = ["apple", "banana", "cherry"]  # list
x = ("apple", "banana", "cherry")  # Tuple
x = range(6)
print("--->", type(x))
print(x)
for i in x:
    print("> Pranavi", i)

x = range(1,11)
for i in range(1,11):
    print()

x = {"name" : "John", "age" : 36}
x = {"apple", "banana", "cherry"}
x = frozenset({"apple", "banana", "cherry"})
x = True 
x = b"Hello"
print("24-->", type(x))
print(x)
x = bytearray(6)
print(x)  # The b'\x00\x00\x00\x00\x00' part is a bytes object containing five bytes, each with the value 0 (\x00 is the hexadecimal representation of 0).
x = memoryview(bytes(5))
print("id is address:",hex(id(x)))
print(x)

