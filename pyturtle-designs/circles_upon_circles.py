import turtle

window = turtle.Screen()
window.setup(width=800, height=600, startx=10, starty=0.5)
mojo = turtle.Turtle() 
mojo.shape("turtle")
scale = 5  

# Move the turtle over to the left 
mojo.penup()
mojo.setpos(-390, 0)
mojo.pendown()
mojo.speed(0)

current = 0   # Here's how we know where we are
seen = set()  # Here's where we'll keep track of where we've been
x = 0
colors = ["light blue", "yellow", "purple", "orange", "green", "blue", "gray", "red", "black"]
# Step increases by 1 each time
for step_size in range(1, 100):

    backwards = current - step_size

    # Step backwards if its positive and we've never been there before
    if backwards > 0 and backwards not in seen:
        mojo.setheading(90)  # 90 degrees is pointing straight up
        mojo.pencolor(colors[x])
        x += 1
        if x > 8:
          x = 0
        # 180 degrees means "draw a semicircle"
        mojo.circle(scale * step_size/2, 180)
        current = backwards
        seen.add(current)

    # Otherwise, go forwards
    else:
        mojo.setheading(270)  # 270 degrees is straight down
        mojo.circle(scale * step_size/2, 180)
        current += step_size
        seen.add(current)

turtle.done()