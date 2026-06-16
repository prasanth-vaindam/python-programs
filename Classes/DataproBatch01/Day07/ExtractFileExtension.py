file_name = input("Enter the file name: ")

pos = file_name.rfind(".")
pos += 1 # pos = pos + 1
print(file_name[pos:])