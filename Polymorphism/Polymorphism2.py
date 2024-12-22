class Shape:
    def area(self):
        return ""
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width= width
    def area(self):
        return f"Rectangle area: {self.length *self.width}"
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius= radius
    def area(self):
        return f"Circle area: {3.14 * self.radius * self.radius}"

class Triangle(Shape):
    def __init__(self,base,height):
        self.base= base
        self.height=height
    def area(self):
        return f"Triangle area: {0.5 * self.base * self.height}"
    
shape_instance= [Shape(),Rectangle(5,3),Circle(5),Triangle(8,6)]

for shape in shape_instance:
    print(shape.area())

    



