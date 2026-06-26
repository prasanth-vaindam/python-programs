msg = input("Enter String:")
print(msg)
reverse = msg[::-1]
print(reverse)

if msg == reverse:
    print("It's a palindrome")
else:
    print("It's not a palindrome")

