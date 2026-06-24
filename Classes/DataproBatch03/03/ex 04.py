age = int(input("Age: "))
vision = input("Vision Test Passed (yes/no): ").lower()
medical = input("Medical Fit (yes/no): ").lower()

if age >= 18 and vision == "yes" and medical == "yes":
    print("Eligible for Driving License")
else:
    print("Not Eligible")
    print("thanks")
print("Welcome")
