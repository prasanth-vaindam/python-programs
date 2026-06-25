marks = int(input("Marks: "))
income = int(input("Annual Family Income: "))
disabled = input("Disabled (yes/no): ").lower()

if (marks >= 90 and income < 300000) or disabled == "yes":
    print("Scholarship Approved")
else:
    print("Scholarship Not Approved")