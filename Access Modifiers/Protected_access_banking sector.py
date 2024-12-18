class Bank:
    def __init__(self,balance):
        self._balance= balance
    def deposite(self,amount):
        self._balance += amount
        print(f" The balance of that account is: {self._balance}")

class SavingsAccount(Bank):
    def apply_interest(self, interest):
        self._balance += (self._balance*interest)/100
        print(f" Total savings account balance is: {self._balance}")


bank_instance=SavingsAccount(50)
bank_instance.deposite(50)
bank_instance.apply_interest(2)


