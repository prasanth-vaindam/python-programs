year = int(input("Enter Year"))
if year % 400==0:
    print("400 Leap Year")
elif year % 100 ==0:
    print("not a Leap Year")
elif year % 4 == 0:
    print("4 Leap Year")
else:
    print("Not a Leap Year")

# if (year%400==0 ) or (year%100!=0 and year%4==0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")