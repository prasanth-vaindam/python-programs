amount = float(input("Purchase Amount: "))
premium = input("Premium Member (yes/no): ").lower()
active = input("Account Active (yes/no): ").lower()

if (amount >= 1000 or premium == "yes") and active == "yes":
    print("Discount Applied")
else:
    print("No Discount")