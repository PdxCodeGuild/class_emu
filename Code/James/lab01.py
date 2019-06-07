# lab01.py

# import turtle
# turtle.forward(100)
# turtle.done()

# imports the turtle module
from turtle import *

from sys import *
# designates the fill color as red
fillcolor("red")
# designates the speed
speed(2)
# designates the width
width(5)

begin_fill()


# for i in range(4)
moves = [1, 2, 3, 4]
for move in moves:
    forward(100)
    left(90)
forward(50)
end_fill()

right(90)
forward(40)
left(90)
forward(100)
back(200)
forward(100)
right(90)
forward(100)
right(30)
forward(100)
back(100)
right(60)
forward(100)
left(90)
penup()
forward(100)
right(90)
forward(100)
pendown()

beginfill("black")
forward(100)
back(20)
left(90)
forward(10)
left(90)
forward(10)
left(90)
forward(10)
right(90)
forward(50)
right(90)
forward(10)
right(90)
forward(10)
right(90)
forward(10)
right(90)




done()
