class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder= account_holder
        self._account_number="424110456789"
        self.__balance= balance

    #public methods
    def display_account_details(self):
        print(f"Account Holder name is:{self.account_holder}")
        print(f"Account Number: {self._account_number}")

    def deposit(self,amount):
        self.__balance+=amount
        print(f"Deposited:{amount}")
        #print(f"Current balance: {self.__balance}")

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance-=amount
            print(f"withdrew: {amount}")
            #print(f"Balance after withdrawl:{self.__balance}")
        else:
            print("Withdrawl not possible.")

    def get_balance(self):
        return self.__balance
    def set_balance(self,amount):
        if amount<0:
            print("Balance is nil")
        else:
            self.__balance= amount

account_instance=BankAccount("Ankita Ghosh", 100345)
account_instance.display_account_details()
account_instance.deposit(1000)
account_instance.withdraw(300)
print(f"Current Balance: {account_instance.get_balance()}")
