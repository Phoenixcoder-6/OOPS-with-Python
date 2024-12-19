from abc import ABC, abstractmethod
import math

#Abstract Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi * self.radius * self.radius
    def perimeter(self):
        return 2* math.pi * self.radius
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length= length
        self.width= width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2*(self.length + self.width)
    

circle_instance= Circle(6)
print(f"Circle area: {circle_instance.area():.2f}")
print(f"Circle Perimeter:{circle_instance.perimeter():.2f}")

rectangle_instance=Rectangle(4,7)
print(f"Rectangle area: {rectangle_instance.area():.2f}")
print(f"Rectangle Perimeter:{rectangle_instance.perimeter():.2f}")