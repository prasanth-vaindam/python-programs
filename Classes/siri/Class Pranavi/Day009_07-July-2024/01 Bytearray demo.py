ba = bytearray(b'\x00\x01\x02\x03\x04')
print(ba)  # Output: bytearray(b'\x00\x01\x02\x03\x04')

# Modify the byte at index 2
ba[2] = 255
print(str(ba))  # Output: bytearray(b'\x00\x01\xff\x03\x04')
