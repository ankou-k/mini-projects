import turtle

pen = turtle.Turtle()

pen.color("pink") #color of turtle
pen.pencolor("black") 
pen.forward(100)

pen.speed(0)

size = 10
a = 20

for i in range(1, a + 1, 1):
  pen.circle(size * i)
  pen.pencolor(0.60 +0.01*i,0.40,1.00)

pen.right(50)
pen.forward(30)

for i in range(1, a + 1, 1):
  pen.circle(size * i)
  pen.pencolor(0.60 +0.01*i,0.40,1.00)
