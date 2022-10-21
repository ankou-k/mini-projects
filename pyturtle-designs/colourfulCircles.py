import turtle

circle = turtle.Turtle()

circle.color("purple")
circle.speed(0)

for a in range(40):
  circle.forward(50)
  circle.right(125)
circle.penup()
circle.goto(50, 50)
circle.pencolor("green")
circle.pendown()

for a in range(20):
  circle.forward(70)
  circle.right(200)

circle.penup()
circle.goto(-40, -40)
circle.pencolor("green")
circle.pendown()

for a in range(20):
  circle.forward(50)
  circle.right(140)

circle.penup()
circle.goto(-20, 60)
circle.pencolor("blue")
circle.pendown()

for a in range(20):
  circle.forward(50)
  circle.right(140)

circle.penup()
circle.goto(-50,-20)
circle.pencolor("orange")
circle.pendown()

for a in range(20):
  circle.forward(50)
  circle.right(140)