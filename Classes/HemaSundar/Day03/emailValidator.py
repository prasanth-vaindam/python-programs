email = input("Enter email address: ")

hasAt = email.__contains__("@")
hasDotCom = email.endswith(".com")
hasDotCodotIn = email.endswith(".co.in")

if hasAt and (hasDotCodotIn or hasDotCom):
    print("Valid EMail address")
else:
    print("Invalid email address")
