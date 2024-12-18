class BankAccount:
    def __init__(self,amount):
        self.__balance= amount

    def deposit(self,amount):
        self.__balance+= amount
        print(f"{amount} deposited.")

    def withdraw(self,amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"{amount} deducted successfully.")
        else:
            print(f"Withdrawl not possible")

    def showbalance(self):
        print(f"The available balance is:{self.__balance}")


bank_instance= BankAccount(100)
bank_instance.showbalance()
bank_instance.deposit(100000)
bank_instance.showbalance()
bank_instance.withdraw(100)
bank_instance.showbalance()