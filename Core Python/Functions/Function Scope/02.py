def bank_account():

    balance = 1000

    def deposit(amount):

        nonlocal balance

        balance += amount

        print("Balance =", balance)

    return deposit

account = bank_account()
account(100)
account(500)