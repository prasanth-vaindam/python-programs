# Program to check if the given number is armstrong or not

def is_armstrong(number):
    temp = number
    armstrong = 0
    while temp > 0:
        reminder = temp % 10
        armstrong = armstrong + reminder * reminder * reminder
        temp //= 10

    if armstrong == number:
        return True
    else:
        return False


# list_of_armstrong_numbers = []
#
# for i in range(1, 4679307775):
#     if is_armstrong(i):
#         list_of_armstrong_numbers.append(i)
#
# print(list_of_armstrong_numbers)

while True:
    if is_armstrong(int(input("Enter a number to check if it is armstrong: "))):
        print("The Given Number is Armstrong!")
    else:
        print("Not an Armstrong Number")
