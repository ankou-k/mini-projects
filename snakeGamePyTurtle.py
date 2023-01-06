import turtle
import time
import random

#game window setup
wn = turtle.Screen()
wn.setup(width=400, height=400)
wn.title("Snake Game")
wn.bgcolor("dark blue")
wn.tracer(0)

#turtle head setup
head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"

#food
food = turtle.Turtle()
food.color("orange")
food.speed(0)
food.shape("circle")
food.penup()
food.goto(-50, 20)

#variables setup
score = 0
highscore = 0
delay = 0.1
parts = []

#write tool setup 
pen = turtle.Turtle()
pen.color("orange")
pen.speed(0)
pen.shape("circle")
pen.penup()
pen.goto(0, 160)
pen.hideturtle()
pen.write("Score: 0 Highscore: 0", align="center", font=("Courier", 15, "normal"))

def go_up():
  if head.direction != "down":
    head.direction = "up"

def go_down():
  if head.direction != "up":
    head.direction = "down"

def go_right():
  if head.direction != "left":
    head.direction = "right"

def go_left():
  if head.direction != "right":
    head.direction = "left"

def move():
  if head.direction == "right":
    x = head.xcor()
    head.setx(x + 10)

  if head.direction == "left":
    x = head.xcor()
    head.setx(x - 10)

  if head.direction == "up":
    y = head.ycor()
    head.sety(y + 10)

  if head.direction == "down":
    y = head.ycor()
    head.sety(y - 10)

#keyboard bindings
wn.listen()
wn.onkeypress(go_up, 'Up')
wn.onkeypress(go_right, 'Right')
wn.onkeypress(go_down, 'Down')
wn.onkeypress(go_left, 'Left')

#main game loop
while True:
  wn.update()

  #wall collision
  if head.xcor() <= -180 or head.xcor() >= 180 or head.ycor() <= -180 or head.ycor() >= 180:
    time.sleep(1)
    head.goto(0,0)
    head.direction = "stop"

    for part in parts:
      part.goto(1000,1000)
    parts.clear()
    score = 0
    delay = 0.1
    pen.clear()
    pen.write("Score: 0 Highscore: {}".format(highscore), align="center", font=("Courier", 15, "normal"))
  
  #food collision
  if head.distance(food) < 8:

    new_part = turtle.Turtle()
    new_part.shape("square")
    new_part.color("green")
    new_part.penup()
    parts.append(new_part)

    score += 1 #add 1 to the score
    delay -= 0.001 #make delay shorter

    if score > highscore:
      highscore = score
    
    pen.clear()
    pen.write("Score: {} Highscore: {}".format(score, highscore), align="center", font=("Courier", 15, "normal"))

    x = random.randint(-140, 140)
    y = random.randint(-140, 140)
    food.goto(x,y)

  for index in range(len(parts)-1, 0, -1):
    x = parts[index-1].xcor()
    y = parts[index-1].ycor()
    parts[index].goto(x,y)
  
  if len(parts) > 0:
    x = head.xcor()
    y = head.ycor()
    parts[0].goto(x,y)
  
  move()
  
  for part in parts:
    if head.distance(food) < 8:
      pass
    

  time.sleep(delay)

wn.mainloop()
