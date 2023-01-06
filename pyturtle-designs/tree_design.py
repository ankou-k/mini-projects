import turtle
#from turtle import *
tree = turtle.Turtle()

turtle.colormode(255)

tree.screen.bgcolor(120, 255, 170)
tree.color(5, 55, 5)
tree.pensize(5)
tree.speed()

tree.left(90)
tree.goto(0, -50)
#tree.forward(50)

def draw_branch(size):
  if size < 4:
    return
  else:
    tree.forward(size)
    tree.left(30)
    #this can be changed to make the tree look different!
    draw_branch(3*size/4)
    tree.right(60)
    draw_branch(3*size/4)
    tree.left(30)
    tree.backward(size)

draw_branch(80)