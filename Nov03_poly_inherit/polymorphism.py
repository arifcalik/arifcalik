import math
class Shape:

    def __init__(self, color):
        self._color = color
    
    def area(self):
        print("I cant have an area, i m virtual")

    def perimeter(self):
        print("I cant have a perimeter, i m virtual")      
    
    def __str__(self):
        return f"I m just a {self.color} shape!"

class Circle(Shape):

    def __init__(self, color, radius=0):
        super().__init__(color)
        self._radius = radius

    def __str__(self):
        return f"I m a circle with {self._radius} cm radius!"       

    def area(self):
        return math.pi * self._radius ** 2

    def perimeter(self):
        return 2 * math.pi * self._radius

class Rectangle(Shape):

    def __init__(self, color, width, length):
        super().__init__(color)
        self._width = width
        self._length = length

    def __str__(self):
        return f"I m a rectangle with {self._width} cm width and {self._length} cm length!"       

    def area(self):
        return self._width * self._length

    def perimeter(self):
        return 2 * (self._width + self._length)

class Triangle(Shape):

    def __init__(self, color, a, b, c):
        super().__init__(color)
        self._a = a
        self._b = b
        self._c = c                

    def __str__(self):
        return f"I m a triangle with {self._a}, {self._b} and {self._c} cm edges!"       

    def area(self):
        p = (self._a + self._b + self._c) / 2
        return (math.sqrt(p * (p - self._a) * (p - self._b) * (p - self._c)))

    def perimeter(self):
        return self._a + self._b + self._c

def main():
    circle = Circle("Red", 4)
    rectangle = Rectangle("Yellow", 2, 3)
    triangle = Triangle("Green", 5, 13, 12)    

    print(circle)
    print(f"My area is {circle.area():.2f} cm-square and my perimeter is {circle.perimeter():.2f} cm")
    print(rectangle)
    print(f"My area is {rectangle.area():.2f} cm-square and my perimeter is {rectangle.perimeter():.2f} cm")    
    print(triangle)
    print(f"My area is {triangle.area():.2f} cm-square and my perimeter is {triangle.perimeter():.2f} cm")    

if __name__ == '__main__':
    main()



