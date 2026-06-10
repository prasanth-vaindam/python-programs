# and ==> if both arguments are True then only result is True
# or ==> if at least one argument is True then result is True
# not ===> complement
print(True and False)  # False
print(True or False)  # True
print(not False)  # True

# For Non-Boolean Types Behaviour:
# 0 is False
# non-zero means True
# empty string is always treated as False

# x and y:
# if x is evaluating to false return x otherwise return y
print(10 and 20)
print(0 and 20)

# x or y:
# if x is evaluating to True then result is x otherwise result is y
print(10 or 20)  # 10
print(0 or 20)  # 20

# not x
# if x is evaluating to True then result is False otherwise True
print(not 10)  # False
print(not 0)  # True

print("Prasanth" and "Srikanth")
print("Yes" or "No")
print("Prasanth" and "")
print(f""" {"" and "google"} """)
print("" or "google")

