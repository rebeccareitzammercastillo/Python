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

account1.make_deposit(50).make_deposit(100).make_deposit(20).make_withdrawal(20).yield_interest().display_account_info()

account2.make_deposit(50).make_deposit(50).make_withdrawal(100).make_withdrawal(200).make_withdrawal(5).yield_interest().display_account_info()