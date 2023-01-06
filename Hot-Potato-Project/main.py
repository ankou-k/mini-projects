from dodge_the_dynamite_turtle import *
import random

def make_queue():
  return []

def enqueue(queue, add):
  queue.append(add)

def dequeue(queue):
  return queue.pop(0)

def size(queue):
  return len(queue)

def remove(queue, player):
  if player in queue:
    queue.remove(player)

def wl(num, players):
  wl_value = make_queue()
  for pl in players:
    enqueue(wl_value, pl)
  
  while size(wl_value) > 1:
    for i in range(num):
      player_bomb = dequeue(wl_value)
      
      bomb.showturtle()
      bomb.penup()
      move_bomb(player_bomb)

      enqueue(wl_value, player_bomb)
    
    dead_person = dequeue(wl_value)
    move_bomb(dead_person)
    explode_bomb(dead_person)
    cancel_name(dead_person, players)

    print(dead_person, " is out of the game")
  
  print(wl_value[0], " is the winner!")

def play():
  print("Welcome to the game......")
  
  answer = int(input("How many players are there?"))

  player_list = []

  for i in range(answer):
    player_list.append(input("Enter name: "))
  
  turns = random.randint(1, answer)

  game_circle(answer, player_list)

  return wl(turns, player_list)

play()