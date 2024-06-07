# Program to check if the given number is Amstrong

def is_amstrong(n):
    temp_number = n
    reminder = 0
    while temp_number > 0:
        t = temp_number % 10
        t = t * t * t
        reminder += t
        t = 0
        temp_number //= 10
    print(reminder)
    if reminder == n:
        return True
    else:
        return False


if is_amstrong(int(input("Enter a number to check if it is amstrong number: "))):
    print("Yes it's an amstrong number!")
else:
    print("No it's not an amstrong number!")

