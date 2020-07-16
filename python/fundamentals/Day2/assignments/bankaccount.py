class BankAccount:
    def __init__(self,balance,int_rate):
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

george = BankAccount(0.00,0.01)
thomas = BankAccount(0.00,0.02)

george.deposit(100.00).deposit(100.00).deposit(100.00).withdraw(40.00).yield_int().display_account_info()
thomas.deposit(2000.00).deposit(1500.00).withdraw(100.00).withdraw(100.00).withdraw(100.00).withdraw(100.00).yield_int().display_account_info()
