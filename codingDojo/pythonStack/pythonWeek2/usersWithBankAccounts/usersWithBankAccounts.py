class BankAccount:
    accounts = []
    def __init__(self,int_rate,account_balance):
        self.int_rate = int_rate
        self.account_balance = account_balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self,amount):
        if(self.account_balance - amount) >= 0:
            self.account_balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.account_balance -= 5
        return self
    
    def display_account_info(self):
        return f"Balance: {self.account_balance}"

    def yeild_interest(self):
        if self.account_balance > 0:
            self.account_balance += (self.account_balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()
class User:
    def __init__(self,name):
        self.name = name
        self.account = {
            "checking" : BankAccount(0.01, 100),
            "savings" : BankAccount(0.05, 200)
        }
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(self.account.account_balance)

    def make_withdraw(self,amount):
        self.account.withdraw(amount)
        print(self.account.account_balance)
    
    def display_user_balance(self):
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
        return self

bryton = User("Bryton")

bryton.account["checking"].deposit(10).deposit(20).deposit(40).withdraw(600).yeild_interest().display_account_info()
bryton.account["savings"].deposit(100).deposit(200).deposit(400).withdraw(60).yeild_interest().display_account_info()