age = int(input("enter your age: "))

# print(age>=18)
if age >= 18:
    print("Your age is", age)
    print("You can Vote")
else:
    print("Your age is", age)
    print("Wait",(18 - age), "Years to vote")

print("thanks")