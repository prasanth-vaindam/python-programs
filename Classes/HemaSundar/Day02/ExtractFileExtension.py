file_name = input("Enter File Name")

pos = file_name.rfind(".")

if pos != -1:
    print(file_name[pos+1:])