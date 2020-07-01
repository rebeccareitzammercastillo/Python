class BankAccount:
    def __init__(self, int_rate, balance):
        self.interest= int_rate
        self.balance= balance

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawal(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance>0:
            self.balance += self.balance * self.interest
        else:
            pass
        return self

account1= BankAccount(.05, 100)
account2= BankAccount(.03, 200)


class User:
    def __init__(self,name_param):
        self.name=name_param
        self.checkings = BankAccount(int_rate=.02, balance=0)
        self.savings = BankAccount(int_rate=.05, balance=100)

    def make_deposit (self, amount):
        self.checkings.make_deposit(amount)
        return self

    def make_withdrawal (self, amount):
        self.checkings.make_withdrawal(amount)
        return self

    def display_user_balance (self):
        print(f'User name: {self.name} Account Balance:{self.checkings.balance}')
        return self
    
    def transfer_money(self,otheruser,amount):
        self.account_balance -= amount
        otheruser.account += amount
        return self

user1= User('Ellie')
user2= User('Schmidt')
user3= User('Edgar')

user1.make_deposit(100).display_user_balance()