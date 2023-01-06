import turtle

window = turtle.Screen()
pen = turtle.Turtle()

window.setup(width=400, height=400)

pen.pensize(10)

colors = ["yellow", "purple", "orange", "pink", "yellow", "purple", "orange", "pink", "yellow", "purple", "orange", "pink", "yellow", "purple", "orange", "pink", "yellow", "purple", "orange", "pink"]

for item in colors:
  pen.pencolor(item)
  if item == "yellow":
    pen.forward(20)
    pen.left(135)
  elif item == "purple":
    pen.forward(30)
    pen.right(39)
  elif item == "orange":
    pen.forward(45)
    pen.left(67)
  elif item == "pink":
    pen.forward(19)
    pen.right(91)