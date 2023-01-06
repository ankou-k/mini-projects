import random
from hangman_pics import HANGMANPICS

def display_board(HANGMANPICS, correct_letters, wrong_letters, word):
  print(HANGMANPICS[len(wrong_letters)])
  print("you have taken " + str(len(wrong_letters)) + " wrong guesses:")
  for letter in wrong_letters:
    print(letter)

  blanks = '_' * len(word)
  for i in range(len(word)):
    if word[i] in correct_letters:
      blanks = blanks[:i] + word[i] + blanks[i+1:]

  print(blanks)

def get_random_word(word_list):
  split_words = word_list.split()
  random_number = random.randint(0, len(split_words) -1)
  return split_words[random_number]

def get_guess(already_guessed_letters):
  while True:
    guess = input("Guess a letter ")
    guess = guess.lower()
    if len(guess) != 1:
      print('please enter only one letter')
    elif guess not in "qwertyuiopasdfgjklzxcvbnm":
      print('please enter a letter in the latin alphabet')
    elif guess in already_guessed_letters:
      print('you already guessed that letter')
    else:
      return guess
      
#setup
print("Hello! Welcome to hangman!")
words = "airplane orange yellow forty lightbulb switch worth quick quack north orlando wonders reality creak"
correct_letters = ""
wrong_letters = ""
game_over = False
my_word = get_random_word(words)

while True:
  display_board(HANGMANPICS, correct_letters, wrong_letters, my_word)
  guess = get_guess(correct_letters + wrong_letters)
  if guess in my_word:
    correct_letters = correct_letters + guess
    #check for win
    win = True
    for i in range(len(my_word)):
      if my_word[i] not in correct_letters:
        win = False
        break
    #check win
    if win:
      print("You guessed the word " + my_word + "!!!!")
      game_over = True
  else:
    wrong_letters = wrong_letters + guess
    if len(HANGMANPICS)-1 == len(wrong_letters):
      print("You've lost!")
      print("The word was " + my_word)
      game_over = True

    if game_over == True:
      answer = input("Do you want to play again? yes/no ")
      answer.lower()
      if answer == "yes":
        my_word = get_random_word(words)
        correct_letters = ""
        wrong_letters = ""
        game_over = False
      else:
        break
