from abc import ABC, abstractmethod

#Define multiple interfaces
#Abstract base class/ Interface
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self,amount):
        pass
class NotificationService(ABC):
    @abstractmethod
    def send_notification(self,message):
        pass

#Implementing Multiple Interfaces in a class
class OnlineStore(PaymentProcessor,NotificationService):
    def process_payment(self, amount):
        print (f"Processing payment of ${amount} ")
    def send_notification(self, message):
        print (f"Notification: {message} ")

store_instance= OnlineStore()
store_instance.process_payment(3000)
store_instance.send_notification("Payment successful!!")

