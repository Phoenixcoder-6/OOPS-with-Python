class Bird:
    def fly(self):
        return "Bird flies"
class Plane:
    def fly(self):
        return "Plane flies"
    
def demonstrate_object(obj):
    print(obj.fly())

bird_instance= Bird()
plane_instance= Plane()

demonstrate_object(bird_instance)
demonstrate_object(plane_instance)
