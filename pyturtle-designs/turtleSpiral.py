import turtle

window = turtle.Screen()
pen = turtle.Turtle()

from turtle import *
penup()
color("light blue")
shape("turtle")
#pen.pendown()
for i in range(40, -1, -1):
  stamp()
  left(i)
  forward(30)