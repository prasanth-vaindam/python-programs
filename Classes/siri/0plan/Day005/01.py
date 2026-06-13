# 1. Voting Eligibility (and)
age = int(input("Enter age: "))
has_id = input("Do you have voter ID (yes/no)? ")

if age >= 18 and has_id == "yes":
    print("Eligible to Vote")
else:
    print("Not Eligible")