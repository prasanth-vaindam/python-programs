filename = input("File Name")

pos = filename.rfind(".")
print(filename[pos+1:])