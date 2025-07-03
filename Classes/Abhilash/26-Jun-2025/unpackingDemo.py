

studentInfo = ["Abhilash", "ICFAI College",  "Hyderabad",
               "24STUCHH010639", 18, 100, 200, 300]

# unpacking

# a, b, c, d, e = studentInfo
# print(f"{a} and {b}")
a, b, c, d, e, *remainingList = studentInfo
print(a)
print(b)
print(c)
print(d)
print(e)
print(remainingList)
