class User:
    def __init__(self,name,email):
        self.name = name 
        self.email = email
        self.account_balance = 0

#methods
    def make_deposit(self,amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print(self.name+", Balance: $"+str(self.account_balance))
        return self

    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(f"{other_user.name} received my money and her balance is ${other_user.account_balance}")
        return self

#instances
maria = User("Maria","mariahernandez@gyahoo.com") 
janice = User("Janice","misschanandlerbong@yhotmail.com") 
winston = User("Winston","winstonchurchill@uk.gov") 

#1 Have the first user make 3 deposits and 1 withdrawal and then display their balance
#2 Have the second user make 2 deposits and 2 withdrawals and then display their balance
#3 Have the third user make 1 deposits and 3 withdrawals and then display their balance

maria.make_deposit(100.00).make_deposit(100.00).make_deposit(100.00).make_withdrawal(50.00).display_user_balance()
janice.make_deposit(5000.50).make_deposit(976.25).make_withdrawal(40.00).make_withdrawal(20.00).display_user_balance()
winston.make_deposit(25.00).make_withdrawal(10.00).make_withdrawal(10.00).make_withdrawal(4.75).display_user_balance()

#BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
maria.transfer_money(janice,150.00).display_user_balance()
