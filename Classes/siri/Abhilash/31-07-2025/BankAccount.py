class BankAccount:
    _minimum_opening_balance = 1000  # Class variable
    balance = 0  # Class variable

    def __init__(self, account_holder):
        self.account_holder = account_holder  # Instance variable
        # balance = 0  # Instance variable

    # def deposit(self, amount):
    #     self.balance = self.balance + amount
    #     print(f"{self.account_holder}'s Balance after Deposit: ", self.balance)
    #
    # def withdraw(self, amount):
    #     if self.balance > amount > 0:
    #         self.balance = self.balance - amount
    #         print(f"{self.account_holder}'s Balance after withdrawal", self.balance)
    #     else:
    #         print(f"{self.account_holder}'s account has insufficient funds or invalid withdrawal amount. Current "
    #               f"balance:", self.balance)


ambaniAc = BankAccount("Ambani")
tataAC = BankAccount("Tata")
print(ambaniAc.minimum_opening_balance)
print(tataAC.minimum_opening_balance)

BankAccount.minimum_opening_balance = 5000  # Changing class variable for all instances
ambaniAc.balance = 2000
ambaniAc.minimum_opening_balance = 3000  # Changing instance variable for ambaniAc
print("minimum balance for ambani", ambaniAc.minimum_opening_balance)
print("minum banalce for tata", tataAC.minimum_opening_balance)
print("Ambani's balance:", ambaniAc.balance)
print("Tata's balance:", tataAC.balance)
# ambaniAc.balance = 5000
print("Ambani's balance:", ambaniAc.balance)
print("Tata's balance:", tataAC.balance)
print("Tata's balance:", tataAC.balance)
# tataAC.deposit(500)

# ambaniAc.deposit(1000)
# ambaniAc.withdraw(100)
# Uncomment the line below to test withdrawal with insufficient funds
# ambaniAc.withdraw(1000)
print("Tata's balance:", tataAC.balance)