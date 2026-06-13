balance = 5000
amount = int(input("Enter amount: "))

if amount <= balance and amount > 0:
    print("Withdrawal Successful")
else:
    print("Insufficient Balance")