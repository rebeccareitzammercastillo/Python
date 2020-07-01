class User:
    def __init__(self,name_param):
        self.name=name_param
        self.account_balance=0

    def make_deposit (self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal (self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance (self):
        print(f'User name: {self.name} Account Balance:{self.account_balance}')
        return self
    
    def transfer_money(self,otheruser,amount):
        self.account_balance -= amount
        otheruser.account_balance += amount
        return self

user1= User('Ellie')
user2= User('Schmidt')
user3= User('Edgar')

user1.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(50)
user1.display_user_balance()


user2.make_deposit(50).make_deposit(50).make_withdrawal(20).make_withdrawal(10)
user2.display_user_balance()

user3.make_deposit(500).make_withdrawal(100).make_withdrawal(10).make_withdrawal(20)
user3.display_user_balance()