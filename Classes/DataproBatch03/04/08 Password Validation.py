password = input("Enter Password: ")

if len(password) >= 8 and not password.isalpha() and not password.isdigit():
    print("Strong Password")
else:
    print("Weak Password")