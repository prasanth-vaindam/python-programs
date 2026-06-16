fullname = input("Enter your name: ")
pos = fullname.rfind(" ") + 1
lastname = fullname[pos:]
print(lastname)