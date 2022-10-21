import turtle

window = turtle.Screen()
pen = turtle.Turtle()

pen.shape("turtle")
pen.forward(40)
pen.left(40)
pen.right(40)

for i in range (5):
  pen.forward(50)
  pen.right(144)

def pastel_star():
  size = 100
  turtle.color("black")
  turtle.width(3)
  angle = 120

  turtle.fillcolor("pink")
  turtle.begin_fill()
  for i in range (5):
    turtle.forward(size)
    turtle.right(angle)
    turtle.forward(size)
    turtle.right(72 - angle)
  turtle.end_fill()

pastel_star()
turtle.forward(200)
pastel_star()

from turtle import *
penup()
for a in range(40, -1, -1):
  stamp()
  left(a)
  forward(20)
