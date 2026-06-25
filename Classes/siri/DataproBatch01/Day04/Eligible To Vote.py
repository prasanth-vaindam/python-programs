age = int(input("enter your age: "))
has_id = bool(input("Do you have voter id? \nYes if you have id otherwise press enter"))

if age >= 18:
    if has_id:
        print("You are eligible to Vote! Choose the right person")
    else:
        print("You have to apply for voter id ")
else:
    print("you need to wait for ", (18-age), "Years in order to Vote")