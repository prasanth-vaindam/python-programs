# program to determine if the given term is a surd
while True:
    base = int(input("Enter the base: "))
    exponent = int(input("Enter the exponent: "))
    root = base ** (1/exponent)

    print(root)
    str_root = str(root)
    str_root_list = str_root.split(".")
    if len(str_root_list[1]) >= 16:
        print("Yes it is a Surd")
    else:
        print("No, it is not a Surd")
