#TODO Import modules.
import random
import hangman_art
import hangman_words
import os


#TODO Show game welcomes and logos.
print(f"\nWELCOME IN HANGMAN GAME")
print(f"{hangman_art.logo}")


#TODO Show menu, with game styles and difficulty. Later, in working app

#TODO Pick a random word from module.
random_word = random.choice(hangman_words.fruits)
print(f"TEST CODE: {random_word}")


#TODO Show underscore for each letter of the word.

#TODO Ask user for input.

#TODO Check lenght of input.

#TODO Validate user guess if it's right or wrong. Wrong means lives -1.

#TODO Check repetitive guesses.

#TODO Clear screen after each guess to avoid full terminal of history.

#TODO Define if user is Winner or Loser.

#TODO Ask to play again or quit.
