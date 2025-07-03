# x = 9
# if x < 5 or x != 7:
#     print("Yes")
# else:
#     print("No ")
#
# a = 1029989.90
# b = 1029989.90
# c = a

# if a == b:
#     print("Yes a == b")
# else:
#     print("No")
#
# if a is b:
#     print("Yes a is b")
# else:
#     print("No a and b are different references ")


# numbers = [1, 2, 3, 4, 5]
# allNumbers = [1, 2, 3, 4, 5]
# # allNumbers = numbers
# if numbers is not allNumbers:
#     print("Yes")
# else:
#     print("No")
#
# word = "hello wheel"
# subString = "eep"
#
# friends = ["giri"]
#
# if "giri" is friends:
#     print("giri is your friend")
# else:
#     print("Giri not in your friends list")
#
# if subString not in word:
#     print("True")
# else:
#     print("False")

"""
program to print reminder  when divided from 2..9 for the given number
walrus operator
floor division - is used when you need to round the value to lower limit - also used in BS
exponent

promised to conduct QUIZ on topics covered so far
is == difference
in list and set
doubt: how real time comparision is done in case of neseted lists , normal list
"""
a = 2
b = 5

# print(a ** b)  # 32 e ^ x power operator
# x = 3
# print(x)  # 3
# print(y := 4)  # 4

# if x := int(input("Enter a number")) >= 4:
#     print(f"the number {x} you entered is 4 or greater than 4") # this is returning Ture
# else:
#     print(f"{x} is less than 4")
#
# if (x := int(input("Enter a number"))) >= 4:
#     print(f"The number {x} you entered is 4 or greater than 4")
# else:
#     print(f"The number {x} you entered is less than 4")


friends = ["ravi", "giri"]
enemies = ["giri", "ravi"]
# when comparing ravi with giri does it use hash values or pure string comparison



# friends = {"ravi", "giri"}
# enemies = {"giri", "ravi"}

# where comparision is done on innere elements and inner sub elements

# Doubt: how elements re compare in sets
# enemies = friends

if friends == enemies:
    print("All are equal before law!")
else:
    print("I am partial towards dharma!")