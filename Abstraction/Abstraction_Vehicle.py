from abc import ABC, abstractmethod
#Abstract Class

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def __init__(self,name):
        self.name= name
    def start(self):
        print(f"{self.name} starts")
    def stop(self):
        print(f"{self.name} stops.")

class Bike(Vehicle):
    def __init__(self,name):
        self.name= name
    def start(self):
        print(f"{self.name} starts")
    def stop(self):
        print(f"{self.name} stops.")

car_instance= Car("Audi")
car_instance.start()
car_instance.stop()

bike_instance= Bike("Porshe")
bike_instance.start()
bike_instance.stop()