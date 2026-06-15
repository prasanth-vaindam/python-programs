# Divisible by 400 → Leap Year
# Otherwise, if divisible by 100 → Not a Leap Year
# Otherwise, if divisible by 4 → Leap Year
# Otherwise → Not a Leap Year

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap Year")
else:
    if year % 100 == 0:
        print("Not a Leap Year")
    else:
        if year % 4 == 0:
            print("Leap Year")
        else:
            print("Not a Leap Year")