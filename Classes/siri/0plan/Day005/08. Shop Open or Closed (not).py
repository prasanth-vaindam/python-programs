# 8. Shop Open or Closed (not)
shop_status = input("is shop open yes / no: ")

print(shop_status)
print(shop_status.lower()) # to change the value to lower case

if shop_status == "yes" or shop_status == "Yes" or shop_status == "YES":
    print("Shop is Open")
else:
    print("Shop is Closed")


