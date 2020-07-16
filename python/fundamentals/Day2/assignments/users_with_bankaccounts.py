class User:
    def __init__(self,name,email):
        self.name = name 
        self.email = email
        self.accounts = []
    def make_deposit(self,amount):
        self.account.balance += amount
        return self
    def make_withdrawal(self,amount):
        self.account.balance -= amount
        return self
    def display_user_balance(self):
        print(self.name+", Balance: $"+str(self.account.balance))
        return self
    def transfer_money(self,other_user,amount):
        self.account.balance -= amount
        # other_account_balance += amount
    def make_account(self,account_name,balance,int_rate):
        new_account = BankAccount(account_name,balance,int_rate)
        self.accounts.append(new_account)
        return self

class BankAccount:
    def __init__(self,account_name,balance,int_rate):
        self.account_name = account_name
        self.balance = balance
        self.int_rate = int_rate
    def deposit(self,amount):
        self.balance += amount
        return self
    def withdraw(self,amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print("Balance: $"+str(self.balance))
        return self
    def yield_int(self):
        if(self.balance > 0):
            self.balance = self.balance*(1+self.int_rate)
        return self

peter = User('Peter','peterpiperpizza@gmail.com')

