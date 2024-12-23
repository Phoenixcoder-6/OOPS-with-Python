from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self):
        pass

class CreditCardPayment(Payment):
    def process_payment(self,amount):
        print(f"Processing a credit card payment of ${amount}")
        print("Transaction Successful!")

class DebitCardPayment(Payment):
    def process_payment(self,amount):
        print(f"Processing a Debit card payment of ${amount}")
        print("Transaction Successful!")

class PayPalCardPayment(Payment):
    def process_payment(self,amount):
        print(f"Processing a PayPal card payment of ${amount}")
        print("Transaction Successful!")


credit_instance= CreditCardPayment()
debit_instance= DebitCardPayment()
pay_instance= PayPalCardPayment()

credit_instance.process_payment(200) 
debit_instance.process_payment(400)
pay_instance.process_payment(56)

