# Senior citizens or students get a discount.
age = int(input("Enter age: "))
is_student = input("Are you a student (yes/no)? ")

if age >= 60 or is_student == "yes":
    print("Discount Available")
else:
    print("No Discount")