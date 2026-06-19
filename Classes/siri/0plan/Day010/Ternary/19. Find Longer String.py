str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

longer = str1 if len(str1) > len(str2) else str2

print("Longer String:", longer)