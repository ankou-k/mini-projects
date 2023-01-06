#print("hello!")
#name = input("What is your name? ")
#print(name)

import turtle
window = turtle.Screen()
pen = turtle.Turtle()
window.bgcolor("black")

pen.color("orange")
pen.shape('turtle')
pen.pensize(2)

for w in range(40):
  pen.fd(60)
  pen.left(130)

pen.penup()
pen.fd(60)
pen.pd()

pen.color("blue")
for w in range(10):
  pen.fd(80)
  pen.left(145)

pen.color("yellow")
for w in range(30):
  pen.fd(70)
  pen.rt(95)

pen.rt(60)

for i in range(4):
  pen.penup()
  pen.fd(80)
  pen.pd()

  for d in range(30):
    pen.fd(1)
    pen.rt(1)

turtle.circle(30)

