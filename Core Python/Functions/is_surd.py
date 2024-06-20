# program, to find the nth root of a number 'a'

n = int(input("enter the exponent: "))
a = int(input("enter the base"))

root = a ** (1/n)
print(root)
root_string = str(root).split(".")
root_string_fraction = root_string[1]

print("length of the fraction part: ", len(root_string_fraction))
if len(root_string_fraction) == 16:
    print("The given root is a surd\n")
else:
    print("Not a surd")
