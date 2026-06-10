def is_armstrong(num):
    # Converting the number to a string to get its length
    num_str = str(num)
    # Calculating the length of the number
    num_digits = len(num_str)
    # Initializing sum to 0
    armstrong_sum = 0

    # Calculating Armstrong sum
    for digit in num_str:
        armstrong_sum += int(digit) ** num_digits

    # Checking if the number is Armstrong
    if armstrong_sum == num:
        return True
    else:
        return False


# Test the function
number = int(input("Enter a number: "))
if is_armstrong(number):
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")
