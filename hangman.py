import random

HANGMAN_PICS = ('''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')

#setup
words = ("tree", "hello", "enigma", "guesswork", "expelliarmus", "grass")
print("Let's play some hangman!!")


def get_random_word(words_list):
  word = random.randint(0, len(words_list)-1)
  return words_list[word]

my_word = get_random_word(words)

game_over = False
correct_letters = ''
wrong_letters = ''

def display_screen(HANGMAN_PICS, wrong_letters, correct_letters, my_word):
  print(HANGMAN_PICS[len(wrong_letters)])
  print("You have gotten " + str(len(wrong_letters)) + " wrong letters!")

  print("wrong letters:")
  print(wrong_letters)

  blanks = "_"*len(my_word)

  for letter in range(len(my_word)):
    if my_word[letter] in correct_letters:
      blanks = blanks[:letter] + my_word[letter] + blanks[letter+1:]
  print(blanks)

def get_guess(already_guessed):
  while True:
    guess = input("Guess a letter: ")
    guess = guess.lower()
    if len(guess) != 1:
      print("Please enter only one letter!")
    elif guess not in "qwertyuiopasdfghjklzxcvbm":
      print("Please enter a letter!")
    elif guess in already_guessed:
      print("You've already guessed this letter!")
    else:
      return guess

while game_over != True:
  display_screen(HANGMAN_PICS, wrong_letters, correct_letters, my_word)

  guess = get_guess(wrong_letters + correct_letters)

  if guess in my_word:
    correct_letters = correct_letters + guess

    win = True #assumption
    for num_letter in range(len(my_word)):
      if my_word[num_letter] not in correct_letters:
        win = False
        break
    
    if win == True:
      print("Congrats! You guessed the word " + my_word)
      game_over = True
  else:
    wrong_letters = wrong_letters + guess

    if len(HANGMAN_PICS)-1 == len(wrong_letters):
      display_screen(HANGMAN_PICS, wrong_letters, correct_letters, my_word)
      print("You lost! The word was " + my_word)
      game_over = True





