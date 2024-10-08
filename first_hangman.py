#TODO Import modules.
import random
import hangman_art
import hangman_words
import os

def make_dict_from_txt():

def welcome_message():

def display_menu():

def pick_random_word():

def create_display():

def get_user_guess():

def update_display():

def clear_screen():

def check_guess():

def is_game_won():

def is_game_lost():

#Main game loop
def play_hangman():


if __name__ == "__main__":
    play_hangman()




#TODO Show game welcomes and logos.
print(f"\nWELCOME IN HANGMAN GAME")
print(f"{hangman_art.logo}")


#TODO Show menu, with game styles and difficulty. Later, in working app

#TODO Pick a random word from module.
random_word = random.choice(hangman_words.fruits)
print(f"TEST CODE: {random_word}")


#TODO Show underscore for each letter of the word.
display =[]
word_lenght = len(random_word)

for _ in range(word_lenght):
    display += "_"


lives = len(hangman_art.stages)-1
end_of_game = False


while not end_of_game:
    print(hangman_art.stages[lives])
    print(f"\nLives: {lives}\n")
    print(f"{' '.join(display)}") #Join list of underscores to str


    #TODO Ask user for input.
    user_guess = input(f"\nGuess a letter: ")

    #TODO Clear screen after each guess to avoid full terminal of history.
    os.system("clear")

    #TODO Check lenght of input.
    if len(user_guess) != 1:
        print("You need guess only 1 letter.\n")
        continue


    #TODO Check repetitive guesses.
    if user_guess in display:
        print(f"You've already guessed the letter {user_guess.upper()} try another one.\n")


    #TODO Check a guessed letter
    for position in range(word_lenght):
        letter = random_word[position].lower()
        if letter == user_guess.lower():
            display[position] = letter


    #TODO Check if user is wrong. -lives counter
    if user_guess not in random_word:
        print(f"Wrong guess you've lost 1 live.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You have lost. The word was: {random_word}")


    #TODO Define win in the game.
    if "_" not in display:
        end_of_game = True
        print(f"You win. You have left {lives} lives.")

print(hangman_art.stages[lives])

    #TODO Ask to play again or quit.
