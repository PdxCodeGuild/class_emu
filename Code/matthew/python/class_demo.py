


# print(type(5))
# print(type('hi'))
# print(type(True))
# print(type(type(5)))


import math


# snake_case_is_like_this
# camelCaseIsLikeThis
# ThisIsPascalCaseOrTitleCase


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def distance(self, p): # method, or 'member function'
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx*dx + dy*dy)
    
    def scale(self, v):
        self.x *= v
        self.y *= v

p3 = Point()
p1 = Point(5,2)
p2 = Point(8,4)

# dist = Point.distance(p1, p2)
dist = p1.distance(p2) # or p2.distance(p1), either works
print(dist)

# similar to how we can call methods of the str class
s = 'hello world'
print(s.split(' '))










class Animal:
    def __init__(self, name):
        self.name = name
    
    def run(self):
        pass

class Squirrel(Animal): # inherit from Animal
    def __init__(self, name, sound='squeak'):
        super().__init__(name) # invoke the parent's initializer
        self.sound = sound
    
    def climb(self):
        pass




def add(a, b):
    return a + b
print(add(5, 7))
print(add('hello ', 'world'))
print(add('hello', 5))




def say_name(animal):
    print(animal.name)

squirrel = Squirrel('Clarence')
print(squirrel.name)
print(squirrel.sound)
squirrel.run()
squirrel.climb()
say_name(squirrel)
say_name([1, 2, 3])





