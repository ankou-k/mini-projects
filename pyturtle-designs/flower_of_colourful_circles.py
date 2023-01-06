import turtle

window = turtle.Screen()
pen = turtle.Turtle()
window.setup(width=200, height=300)
'''
#def function_name(paramteres):
def two_lines(color, length):
  pen.forward(length) #needs a number
  pen.color(color) #needs to be a string
  pen.left(45)
  pen.forward(length)

#do instructions
two_lines("red", 10)
two_lines("blue", 30)
'''
#function to draw a circle of specified size and color
def circle(size, color):
  pen.color(color)
  pen.circle(size)

circle(50, "orange")
pen.speed(0)
colors_list = ["yellow", "red", "purple", "orange", "green", "blue"]

color_num = 0

for count in range(50):
  circle(1*count, colors_list[color_num])
  circle(-1*count, colors_list[color_num])
  pen.left(count)
  color_num = color_num + 1
  if color_num > 5:
    color_num = 0




