import turtle

pen = turtle.Turtle()
pen.color("yellow")

back = turtle.Screen()
back.bgcolor("black")

x = 0

pen.penup()
pen.right(45)
pen.forward(90)
pen.right(135)
pen.pendown()

pen.speed(0)

size = 50

while x < 80:
  pen.forward(size)
  pen.right(61) #1
  pen.forward(size)
  pen.right(61) #2
  pen.forward(size)
  pen.right(61) #3
  pen.forward(size)
  pen.right(61) #4
  pen.forward(size)
  pen.right(61) #5
  pen.forward(size)
  pen.right(61) #6
  pen.right(11.111)
  x = x + 1