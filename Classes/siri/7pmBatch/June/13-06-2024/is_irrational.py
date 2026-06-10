numerator = int(input("enter a numerator: "))
denominator = int(input("enter a denominator must not be zero: "))

if denominator == 0:
    print("Error")

result = numerator / denominator

str_res = str(result)
fractional_part = str_res.split(".")

if len(fractional_part[1]) > 15:
    print("Irrational number")
else:
    print("rational number")

# if count > 15:
#     print("It is Surd!")
# else:
#     print("Not a Surd!")

