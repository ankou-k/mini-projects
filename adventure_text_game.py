def start():
  print("You are in a moist, cold dungeon.")
  input()
  print("The bleak light of torches is barely enough to see. You want to leave this dungeon.")
  input()
  print("There is a door to your left and to your right. ")
  print("Which one do you take?")

  choice = input()
  if choice == "left":
    tunnel_room()
  elif choice == "right":
    forest()
  else:
    dead("You have gotten too weak because of the cold and died.")

def dead(why):
  print(why + " Try again.")

def tunnel_room():
  print("You have entered a tunnel. There are glowing origami floating around.")
  input()
  print("You walk forward, entranced. The origami continue floating and you feel completely at peace.")
  input()
  print("You see a door on the other end of the tunnel, but you are not sure if you want to leave.")
  print("What do you do, leave or stay?")
  answer = input()
  
  if answer == "stay":
    dead("This was a trap.")
  elif answer == "leave":
    forest()
  else:
    dead("You fell asleep because it was taking you so long to decide what to do. The tunnel sucked you into the walls and you died.")

def forest():
  print("The door opens up into a forest. This must be a portal because the dungeon is far under the ground.")
  input()
  print("There is a fawn standing a bit away from the door, looking at you.")
  input()
  print("After locking eyes for a few seconds, the fawn says 'Hello human. What are you doing here?'")
  print("What do you reply?")
  answer = input()
  print("The fawn says 'I can help you go outside into the human world. Do you trust me to help you?'")
  answer = input()
  if answer == "yes" or answer == "yeah":
    fawn()
  else:
    print("The fawn lowers their head and says 'as you wish. The road is tricky, and I wish you the best of luck.'")
    input()
    print("The fawn leaves. You are alone now.")
    input()
    print("You decide to walk forward until you find something.")

def fawn():
  print("The fawn bows their head and turns around. You follow them into the bushes. They lead you down a pathway that you would not have noticed without them.")
  input()
  print("The fawn leads you out of the danger. You've managed to escape the dungeon. You've won the game!")

start()
