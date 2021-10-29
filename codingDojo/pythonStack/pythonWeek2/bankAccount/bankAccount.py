class BankAccount:
    all_accounts = []
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds: charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print("Balance: " + str(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0: 
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def account_display(cls):
        for account in cls.all_accounts:
            account.display_account_info()

Joe = BankAccount(.01,10).deposit(178).deposit(36).deposit(120).withdraw(240).yield_interest().display_account_info()
Smith = BankAccount(.03,104).deposit(1000).deposit(502).withdraw(152).withdraw(21).withdraw(752).withdraw(45).yield_interest().display_account_info()
BankAccount.account_display()