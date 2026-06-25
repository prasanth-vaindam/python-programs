year = int(input("Enter the year: "))

if (year % 400 == 0)  or (year % 100 !=0 and year %4==0):
    print("It's a Leap Year")
else:
    print("It's not a leap year")
