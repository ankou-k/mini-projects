# Turtle functions from here onwards
import turtle

sally = turtle.Turtle()
bomb = turtle.Turtle()
blue_bomb = turtle.Turtle()
explosion = turtle.Turtle()

player_pos = []# [[name, coord]...] pairs created in the game_circle function

#registering the bomb gif into the turtle screen
#change the file path of the gif file below accordingly 
bomb_image = 'bomb.gif'
window = turtle.Screen()
window.register_shape(bomb_image)
bomb.shape(bomb_image)
bomb.hideturtle()

#registering the blue bomb gif into the turtle screen
#change the file path of the gif file below accordingly
blue_bomb_image = 'blue_bomb.gif'
window = turtle.Screen()
window.register_shape(blue_bomb_image)
blue_bomb.shape(blue_bomb_image)
blue_bomb.hideturtle()

#registering the explosion gif into the turtle screen
#change the file path of the gif file below accordingly
explosion_image = 'explosion-animated.gif'
window = turtle.Screen()
window.register_shape(explosion_image)
explosion.shape(explosion_image)
explosion.hideturtle()

#for creating the explosion effect
def explode_bomb(b):
    explosion.penup()
    for player, coord in player_pos:
        if player == b:
            explosion.goto(*coord)
            default = window.delay()
            window.delay(1000)
            explosion.showturtle()
            window.delay(default)
            
            
    explosion.hideturtle()

# move the black bomb around the game circle 
def move_bomb(b):
    for player, coord in player_pos:
        if player == b:
            bomb.speed(1)
            bomb.goto(*coord)

# move the blue bomb around the game circle 
def move_blue_bomb(b):
    for player, coord in player_pos:
        if player == b:
            blue_bomb.speed(1)
            blue_bomb.goto(*coord)


# drawing a circle and writing the names of the participants around the circle
def game_circle(m, players):
    draw_circle()
    
    angle = round(360/m)
    for i in range(m):

        #for aligning the names around the circle
        sally.right(i * angle)
        if 0<i*angle < 90 or 270<i*angle < 360:
            sally.fd ( 200)
        else:
            sally.fd(250)

        player_pos.append([players[i], sally.pos()])# [[name, coord]...] finding the coordinates of each name
        
        sally.write(players[i],font = ("Arial", 15, "normal")) # writing the names of the players around the circle
        sally.home() # go back to the center of the circle


        
## create a strike through function(changing the color of the name from back to red)
def cancel_name(dead, players):
    for player, coord in player_pos:
        if player == dead:
            sally.goto(*coord)
            sally.pencolor('red')
            sally.write(dead, font = ("Arial", 15, "normal"))
            sally.pencolor('black')
    


# code to draw a circle
def draw_circle():
    sally.penup()

    sally.right(90)    # Face South
    sally.forward(200)   # Move one radius
    sally.right(270)   # Back to start heading
    sally.pendown()    # Put the pen back down
    sally.circle(200)    # Draw a circle
    sally.penup()      # Pen up while we go home
    sally.home()  