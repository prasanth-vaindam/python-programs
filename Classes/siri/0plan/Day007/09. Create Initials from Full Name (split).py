name = input("Enter your full name: ")

names = name.split()
initials =""
for name in names:
    # print(name[0], end ="")
    initials += name[0]

print(initials.upper())