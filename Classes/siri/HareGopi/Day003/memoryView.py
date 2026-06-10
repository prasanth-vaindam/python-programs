data = bytearray(b"ABCDE")

view = memoryview(data)

view[0] = 90

print(data)

large_data = bytearray(b"Hello")
copy = large_data[:]   # Creates a new copy
#------
large_data = bytearray(b"Hello")
view = memoryview(large_data)

data = bytearray(100_000_000)
# Suppose you only want to work with a small portion of it.
part = data[1000:5000]
viewPart = memoryview(data)[1000:5000]
