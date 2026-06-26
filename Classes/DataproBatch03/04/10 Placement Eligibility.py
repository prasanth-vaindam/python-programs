cgpa = float(input("CGPA: "))
backlogs = int(input("Backlogs: "))
internship = input("Completed Internship (yes/no): ").lower()

if (cgpa >= 7.5 and backlogs == 0) or internship == "yes":
    print("Eligible for Placement")
else:
    print("Not Eligible")