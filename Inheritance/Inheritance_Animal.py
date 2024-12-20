class Animal:
    def __init__(self,name):
        self.name= name
    def sound(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    
    def sound(self):
        print(f"{self.name} barks. It is a {self.breed}.")

class Cat(Animal):
    def sound(self):
        print(f"{self.name} meows.")


dog_instance= Dog("Buddy","Labrador")
dog_instance.sound()

cat_instance= Cat("Pussy")
cat_instance.sound()

