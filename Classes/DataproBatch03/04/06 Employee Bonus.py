salary = int(input("Salary: "))
experience = int(input("Years of Experience: "))
rating = input("Performance Rating (good/average): ").lower()

if (salary < 50000 and experience >= 5) or rating == "good":
    print("Bonus Granted")
else:
    print("No Bonus")