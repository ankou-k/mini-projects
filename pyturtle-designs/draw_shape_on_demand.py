import turtle

shape = input("What shape do you want to draw? Square, Star or Circle? ")
size = input("What size do you want the shape to be? ")
color = input("What color do you want the shape to be? ")

pen = turtle.Turtle()

def square_draw(size, color):
  pen.fillcolor(color)
  pen.begin_fill()

  for count in range(4):
    pen.forward(size)
    pen.left(90)

  pen.end_fill()

def star_draw(size, color):
  pen.fillcolor(color)
  pen.begin_fill()

  for count in range(5):
    pen.forward(size)
    pen.left(144)

  pen.end_fill()

def circle_draw(size, color):
  pen.fillcolor(color)
  pen.begin_fill()
  pen.circle(size)
  pen.end_fill()

#square_draw(10, "yellow")

if shape == "square":
  square_draw(int(size), color)
elif shape == "star":
  star_draw(int(size), color)
else:
  circle_draw(int(size), color)

#square
#star
#circle