s = "hello"
reverse = ""
for letter in s:
    reverse = letter + reverse

# print(reverse)

i = len(s) -1
reverse=""
while i >=0 :
    print(s[i] , end ="")
    reverse = reverse + s[i]
    i= i - 1

print(f"\n{reverse}")
