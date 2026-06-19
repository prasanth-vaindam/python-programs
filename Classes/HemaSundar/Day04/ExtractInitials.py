sen = "sachin ramesh tendulkar"

names = sen.split()

initial =""
for name in names:
    initial =  initial + name[0].upper()

print(initial)