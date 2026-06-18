s = "hello"
reverse = ""
for letter in s:
    reverse = letter + reverse

# print(reverse)

i = len(s) -1

while i >=0 :
    print(s[i] , end ="")
    i= i - 1
