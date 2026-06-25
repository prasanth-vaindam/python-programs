email_id = input("Enter your email id: ")
hasAt = email_id.__contains__('@')

hasDotCom = email_id.endswith(".com")
hasDotCoDotIn = email_id.endswith(".co")

if hasAt and (hasDotCom or hasDotCoDotIn):
    print("valid email address")
else:
    print("Invalid email address")