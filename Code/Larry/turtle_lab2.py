# turtle_lab2.py
# Draw a stick figure

import turtle
# head
turtle.circle(25)
turtle.right(90)
# neck
turtle.forward(35)
# right arm
turtle.left(115)
turtle.forward(45)
# back to neck
turtle.right(180)
turtle.penup()
turtle.forward(45)
# left arm
turtle.right(55)
turtle.pendown()
turtle.forward(45)
# back to neck
turtle.right(180)
turtle.penup()
turtle.forward(45)
turtle.right(60)
# body
turtle.pendown()
turtle.forward(45)
# right leg
turtle.left(45)
turtle.forward(45)
# back to body
turtle.right(180)
turtle.penup()
turtle.forward(45)
# left leg
turtle.pendown()
turtle.left(90)
turtle.forward(45)
# the end
turtle.done()
