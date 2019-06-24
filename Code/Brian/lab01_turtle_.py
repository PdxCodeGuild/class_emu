# lab1_turtle_V1.py
'''
Lab 1: Turtle
Explanation
Turtle is a python module that allows us to move a virtual turtle around the screen using programming statements. This turtle has a position and a heading.
Below are a list of commands, you can more in the turtle docs.

forward(distance) moves the turtle forward the given number of pixels

left(angle) and right(angle) turns the turtle left or right by the given angle (in degrees)

color(color_name) sets the pen's color, which can be penup() penup() penup()

penup() raises the pen, a line won't be drawn when the turtle moves, pendown() lowers the pen again

setposition(x, y) moves the turtle to the given position

fillcolor(color_name) sets the fill color, begin_fill() indicates you'd like to begin filling in whatever you draw, end_fill() actually fills the shape in.

Use these functions to draw a stick figure with a head, body, two arms, and two legs. Once you're done, go through the examples below and create your own drawing.

Examples
Drawing a Square
from turtle import *

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)

done()
'''
from turtle import * #imports the turtle module
# the below is code for my stick figure with head, body, arms and legs
left(90) #turns/rotates the pen "90" degress to the left
forward(150) #advances the pen 150 pixels (or "px") forward in the direciton it's pointing, drawing a line as it moves
circle(20) #draws a circle, "20"px in diamter
backward(75) #withdraws the pen "75"px backwards, drawing a line as it moves
left(90)
forward(30)
backward(60)
forward(30)
left(90)
forward(75)
left(45)
forward(60)
backward(60)
right(90) #turns/rotates the pen "90" degress to the right
forward(60)
# end of stick figure

# the below is code for my own drawing
up()
forward(150)
down()
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(45)
right(90)
forward(45)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(35)
right(90)
forward(35)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(25)
right(90)
forward(25)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(15)
right(90)
forward(15)
right(90)
forward(10)
right(90)
forward(10)
right(90)
forward(5)
right(90)
forward(5)
right(90)
# end of my own drawing code (sorry, I am not an artist)
done() #lets the system know you are done with the turtle module
