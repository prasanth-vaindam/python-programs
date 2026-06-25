rooms = 5
member = input("Member (yes/no): ").lower()
festival = input("Festival Season (yes/no): ").lower()

if rooms > 0 and (member == "yes" or festival == "no"):
    print("Booking Confirmed")
else:
    print("Booking Not Available")