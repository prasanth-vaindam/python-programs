class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.balance = balance
        self.account_holder = account_holder

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return self.balance


account = BankAccount("John Doe", 1000)
account.deposit(500)
account.withdraw(200)
print(account.balance)