age = int(input("Age: "))
student = input("Student (yes/no): ").lower()
senior = input("Senior Citizen (yes/no): ").lower()

if student == "yes" or senior == "yes" or age < 12:
    print("Discount Ticket")
else:
    print("Regular Ticket")