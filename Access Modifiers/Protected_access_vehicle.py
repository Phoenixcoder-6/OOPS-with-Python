class Vehicle:
    def __init__(self,fuel):
        self._fuel_capacity = fuel

    def display_fuel(self):
        print(f" The updated fuel capacity is : {self._fuel_capacity}")

class Car(Vehicle):
    def refuel_car(self,litres):
        self._fuel_capacity+= litres
        print(f"Refueled with {litres} litres.")
    
car_instance= Car(50)
car_instance.display_fuel()
car_instance.refuel_car(40)
car_instance.display_fuel()