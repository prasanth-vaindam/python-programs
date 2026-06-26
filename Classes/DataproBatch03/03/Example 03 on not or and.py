salary = int(input("Salary: "))
credit = int(input("Credit Score: "))
guarantor = input("Guarantor (yes/no): ").lower()

if (salary >= 50000 and credit >= 700) or guarantor == "yes":
    print("Loan Approved")
else:
    print("Loan Rejected")