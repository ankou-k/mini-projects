import random
from tkinter import *

def calculate():
  heads = 0
  tails = 0
  counter = 0
  flips = myEntry.get()

  if flips == '':
    print("hello")
  else:
    flips = int(flips)
    if flips <= 0:
      errorMessage.set("Amount of flips has to be more than 0!")
    else:
      errorMessage.set('')

      #flip coins
      while counter < flips:
        rand = random.randint(0,1)
        if rand == 0:
          heads += 1
        else:
          tails += 1

        headsAmount.set("Heads: " + str(heads))
        tailsAmount.set("Tails: " + str(tails))
        counter += 1
        


app = Tk()
app.geometry('500x200')
app.title("            Coin Flip!")

#Label
welcomeText = StringVar()
welcomeText.set("Enter a positive amount of flip as number: ")
welcomeMessage = Label(app, textvar=welcomeText)
welcomeMessage.pack()

#Entry
myEntry = Entry(app)
myEntry.pack()

#Output Label
errorMessage = StringVar()
errorMessage.set('')
error = Label(app, textvar=errorMessage)
error.pack()

#Heads
headsAmount = IntVar()
headsAmount.set("Heads: 0")
headLabel = Label(app, textvar=headsAmount)
headLabel.pack()

#Tails
tailsAmount = IntVar()
tailsAmount.set("Tails: 0")
tailLabel = Label(app, textvar=tailsAmount)
tailLabel.pack()

#Submit Button
submit = Button(app, text="Simulate", command=calculate)
submit.pack()

app.mainloop()