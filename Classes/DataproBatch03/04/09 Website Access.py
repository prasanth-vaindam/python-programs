logged_in = True
subscription = False
admin = True

if logged_in and (subscription or admin):
    print("Access Granted")
else:
    print("Access Denied")