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


def create_display(chosen_city):
    """Prompts the user to guess a letter and returns user_guess"""
    return ["_" for _ in range[len(chosen_city)]]


def get_user_guess():
    """Updates the display with correctly guessed letters."""
user_guess = input("Guess a letter: ").lower() # Convert user inpup to lowercase


def update_display(chosen_city, display, user_guess):
    """Updates the display with correctly guessed letters."""
    for position in range(len(chosen_city)):
        letter = chosen_city[position].lower() #C ompare lowercase
        if letter == user_guess: # Compare with user guess
            display[position] = chosen_city[position] # Keep original letter case


def clear_screen():
    """Clear screen after every guess"""
    if os.name == "nt": # Win .. ###NT = new technology means windows os.
        os.system("cls")
    else:
        os.system("clear") # Unix

def check_guess(chosen_city, user_guess, lives):
    if user_guess not in chosen_city.lower():
        print(f"Wrong guess, you've lost 1 life.")
        lives -= 1
    return lives


def is_game_won():

def is_game_lost():




def play_hangman():
    """Main function to run the hangman game."""

    file = "countries-and-capitals.txt"
    countries_dict = make_dict_from_txt(file)

    welcome_message()

    difficulty = display_menu() #Get the difficulty level based on user input 
    show_country = difficulty == 1 #Show country on on level 1
    lives = len(hangman_art.stages) -1 if difficulty < 3 else len(hangman_art.stages2) -1 #set lives based on difficulty

    chosen_city, country = pick_random_word(countries_dict) # Get capital and country
    display = create_display(chosen_city)
    end_of_game = False


if __name__ == "__main__":
    play_hangman()




# while not end_of_game:
#     print(hangman_art.stages[lives])
#     print(f"\nLives: {lives}\n")
#     print(f"{' '.join(display)}") #Join list of underscores to str


#     #TODO Check lenght of input.
#     if len(user_guess) != 1:
#         print("You need guess only 1 letter.\n")
#         continue


#     #TODO Check repetitive guesses.
#     if user_guess in display:
#         print(f"You've already guessed the letter {user_guess.upper()} try another one.\n")


#     #TODO game is lost
#         if lives == 0:
#             end_of_game = True
#             print(f"You have lost. The word was: {random_word}")


#     #TODO Define win in the game.
#     if "_" not in display:
#         end_of_game = True
#         print(f"You win. You have left {lives} lives.")

# print(hangman_art.stages[lives])

#     #TODO Ask to play again or quit.
