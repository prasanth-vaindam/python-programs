file_path = input("Enter filepath: ")
pos = file_path.rfind("\\") + 1

last_folder_name = file_path[pos:]
print(last_folder_name)
