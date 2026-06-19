password = input("Enter password: ")

print("Strong" if len(password) >= 8 else "Weak")