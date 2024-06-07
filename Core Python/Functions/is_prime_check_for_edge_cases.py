# Program to Print if the given number is prime or not

def is_prime(number):
    if number == 1:
        return False

    if number == 2:
        return True
    count = 0
    for i in range(2, number//2+1):
        # print("entered", i)
        # count += 1
        if number % i != 0:
            # print("input number is: ", number)
            continue
        else:
            # print("number is ", number)
            # count += 1
            return False
    return True


listOfPrimesBelow100 = []

for x in range(0, 101):
    print(f" is {x} prime : {is_prime(x)}")
    if is_prime(x):
        listOfPrimesBelow100.append(x)

print(listOfPrimesBelow100)

while True:
    if is_prime(int(input("Enter a number to check if it is Prime or Not: "))):
        print(f"The Given Number is prime!")
    else:
        print("The Given Number is Not Prime!")

