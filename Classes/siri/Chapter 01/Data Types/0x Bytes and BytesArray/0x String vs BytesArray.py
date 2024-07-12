ba = bytearray(b'\x00\x01\x02\x03\x04')
print(ba)  # Output: bytearray(b'\x00\x01\x02\x03\x04')

# Delete the byte at index 1
del ba[1]
print(ba)  # Output: bytearray(b'\x00\x02\x03\x04')

# Delete a slice of bytes
del ba[1:3]
print(ba)  # Output: bytearray(b'\x00\x04')

ba = bytearray(b'Hello')
print(ba)
ba[0:1] = b'Y'
ba[0] = ord('y')
print(ba)

