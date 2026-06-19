text = input("Enter a string: ")

print("Palindrome" if text == text[::-1] else "Not a Palindrome")