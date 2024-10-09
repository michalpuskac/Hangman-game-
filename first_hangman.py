#TODO Import modules.
import random
import hangman_art
import os

def make_dict_from_txt(filename):
    """Read .txt file go through every line and split it on '|' at the end make a dictionary from it. """
    cities_dictionary = {}
    with open(filename, "r", encoding = "utf-8") as file: #utf-8 encoding for for cross platform, (not win default)
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
    return ["_" for _ in range(len(chosen_city))]


def get_user_guess():
    """Updates the display with correctly guessed letters."""
    user_guess = input("Guess a letter: ").lower() #Convert user input to lowercase
    return user_guess

def update_display(chosen_city, display, user_guess):
    """Updates the display with correctly guessed letters."""
    for position in range(len(chosen_city)):
        letter = chosen_city[position].lower() #Compare lowercase
        if letter == user_guess: # Compare with user guess
            display[position] = chosen_city[position] # Keep original letter case


def clear_screen():
    """Clear screen after every guess"""
    if os.name == "nt": # Win .. ###NT = new technology means windows os.
        os.system("cls")
    else:
        os.system("clear") # Unix


def print_game_state(display, lives, country, show_country,difficulty):
    """Prints the current game state of the game, including the hangman graphic, lives, and the guessed word."""
    if difficulty == 3:
        print(hangman_art.stages2[lives])
        print(f"Lives: {lives} / {len(hangman_art.stages2)-1}")
    else:
        print(hangman_art.stages[lives])
        print(f"Lives: {lives} / {len(hangman_art.stages)-1}")
        if show_country: # Only if the difficulty allows display the country
            print(f"Guess the capital of : {country}\n")
        print(f"{' '.join(display)}")  # Display the current guessed letters


def is_game_won(display):
    """Check if the game is won (no more underscores on display)."""
    return "_" not in display


def is_game_lost(lives):
    """Check if the game is lost (no more lives left)."""
    return lives == 0



def play_hangman():
    """Main function to run the hangman game."""
    file = "countries-and-capitals.txt"
    countries_dict = make_dict_from_txt(file)

    welcome_message()

    difficulty = display_menu() #Get the difficulty level based on user input 
    show_country = difficulty == 1 #Show country on on level 1
    lives = len(hangman_art.stages)-1 if difficulty < 3 else len(hangman_art.stages2) -1 #Set lives based on difficulty

    chosen_city, country = pick_random_word(countries_dict) #Get capital and country
    display = create_display(chosen_city)
    end_of_game = False
    all_guesses = []
    wrong_guesses = []

    while not end_of_game:
        print_game_state(display, lives, country, show_country, difficulty)
        if wrong_guesses:
            print(f"Incorrect guess: {', '.join(wrong_guesses)}")
        
        user_guess = get_user_guess()

        if user_guess == "quit": # Quit condition
            print(f"Goodbye")
            break

        clear_screen() #Clear screen history after every guess

        if len(user_guess) != 1: #Check the guess has leght of only one sign
            print(f"You need to guess only 1 letter.\n")
            continue

        if user_guess in all_guesses: #Check if the guess has been made before
            print(f"You've already guessed the letter {user_guess.upper()}, try another one.\n")
            continue

        all_guesses.append(user_guess) #Add guess to the list of all guesses

        if user_guess in chosen_city.lower(): #Correct guess
            update_display(chosen_city, display, user_guess)
        else: #incorrect guess
            if user_guess not in wrong_guesses: #Only loose life if it's new wrong guess
                wrong_guesses.append(user_guess)
                lives -= 1
                print(f"Wrong guess, you've lost 1 life.")

        if is_game_won(display):
            end_of_game = True
            print(f"You win! The capital of {country} is {chosen_city}.")

        if is_game_lost(lives):
            end_of_game = True
            print(f"\nYou have lost.\n")
            print(f"The word was {chosen_city.upper()} the capital of {country}.")

    if difficulty == 3:
        print(f"{hangman_art.stages2[lives]}")
    else:
        print(f"{hangman_art.stages[lives]}")

if __name__ == "__main__":
    play_hangman()