#TODO Import modules.
import random
import hangman_art
import hangman_words
import os

def make_dict_from_txt(filename):
    """Read .txt file go through every line and split it on '|' at the end make a dictionary from it. """
    cities_dictionary = {}
    with open(filename, "r", encoding = "utf-8") as file:
        for line in file:
            line = line.strip()
            if "|" in line:
                country, capital = line.split("|")
                cities_dictionary[capital.strip()] = country.strip() # Capital as key, country as value
    return cities_dictionary

def welcome_message():
    """Print welcome message and logo of a game from hangman_art file."""
    print(f"\nWELCOME TO HANGMAN GAME")
    print(f"{hangman_art.logo}\n")


def display_menu():
    """Displays the game menu and returns the player's chosen difficulty level"""
    print(f"Select difficulty level:")
    print(f"1. Easy (Country is shown)")
    print(f"2. Medium (No country shown)")
    print(f"3. Hard (No country shown, only 3 lives)")

    while True: 
        try:
            difficulty = int(input("Enter difficulty level 1, 2, or 3: "))
            if difficulty in [1,2,3]:
                return difficulty
            else:
                print(f"Please enter a valid choice (1, 2, or 3).")
        except ValueError:
            print(f"Please enter a number (1, 2, or 3).")


def pick_random_word(cities_dictionary):
    """Picks and return random word from word list of hangman words file."""
    random_capital = random.choice(list(cities_dictionary.keys()))
    country = cities_dictionary[random_capital]
    return random_capital, country


def create_display():

def get_user_guess():

def update_display():

def clear_screen():

def check_guess():

def is_game_won():

def is_game_lost():


def play_hangman():
    """Main function to run the hangman game."""

    file = "countries-and-capitals.txt"
    countries_dict = make_dict_from_txt(file)

if __name__ == "__main__":
    play_hangman()



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
