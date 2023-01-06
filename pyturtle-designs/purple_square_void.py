import turtle
pen = turtle.Turtle()
window = turtle.Screen()

width = 300
height = 300

window.setup(width=width,height=height)
window.bgcolor("black")
turtle.colormode(255)
pen.speed(0)
pen.penup()
pen.goto((-width/2)+10, height/2-15)
pen.pendown()

def spiral_draw(line_length, line_color):
  if line_length > 2: #Terminating case
    color_adj = line_color -1
    length_adj = line_length-5
    pen.pencolor(line_color, 0, 255)
    pen.forward(line_length)
    pen.right(90)
    spiral_draw(length_adj, color_adj)

#Base case
spiral_draw(width - 30, 255)