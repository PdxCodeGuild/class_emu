


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, c):
        return ComplexNumber(self.a + c.a, self.b + c.b)

    def __str__(self):
        return f'{self.a} + {self.b}'

num1 = ComplexNumber(5, 2)
num2 = ComplexNumber(3, 4)
num3 = num1 + num2
print(num3)




class Point:
    def __init__(self, x, y): # this is the initializer
        self.x = x # these are member variables
        self.y = y

p = Point(5,2) # call the initializer, instantiate the class
print(p.x) # 5
print(p.y) # 2

print(type(p)) # Point
