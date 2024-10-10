Hangman Game

This is a Python-based Hangman game where you guess the capital cities of countries based on the difficulty level you choose. The game includes three difficulty levels: Easy, Medium, and Hard.

In the Easy mode, the country is displayed alongside the blank spaces representing the letters of the capital city. In the Medium mode, only the blank spaces for the capital are shown. The Hard mode reduces the number of lives and does not display the country name.

Features

	•	Three difficulty levels:
	•	Easy: Country is shown and you have the full set of lives.
	•	Medium: No country is shown but you still have full lives.
	•	Hard: No country is shown and you only get 3 lives.
	•	Cities are randomly chosen from a list of world capitals stored in a .txt file.
	•	ASCII art is used to display the hangman progress and game states.
	•	Full integration with unit tests for game functionality.

Game Demo

WELCOME TO HANGMAN GAME

Select difficulty level:
1. Easy (Country is shown)
2. Medium (No country shown)
3. Hard (No country shown, only 3 lives)

Installation

To run the game locally, follow these steps:

Prerequisites

	•	Python 3.x is required.
	•	The game uses external libraries for ASCII art, so make sure to have the necessary files included in your project.

Steps

	1.	Clone the repository:

git clone https://github.com/your-username/hangman-game.git


	2.	Navigate to the project folder:

cd hangman-game


	3.	Install any required dependencies (if needed):

pip install -r requirements.txt


	4.	Run the game:

python main_hangman.py



Files Structure

	•	main_hangman.py: The main script to run the game.
	•	hangman_art.py: Contains ASCII art and hangman stages.
	•	countries-and-capitals.txt: The file containing country and capital pairs used in the game.
	•	test_hangman.py: Unit tests for the game.

Running the Game

Simply run the following command in the terminal to start the game:

python main_hangman.py

Controls

	•	Input letters to guess the capital.
	•	You can quit the game by typing "quit".

Running the Tests

This project includes unit tests to ensure the game functions as expected. Tests cover functions like reading the data from the .txt file, user input handling, and the game logic for display and lives.

Running Tests

To run the tests, you need to have pytest installed. You can install it using:

pip install pytest

Once installed, run the following command from the project directory:

pytest

Test Example

	•	Test User Input Simulation:

def test_get_user_guess(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "a")
    from main_hangman import get_user_guess
    assert get_user_guess() == "a"


	•	Test Display Update:

def test_print_game_state(capfd):
    display = ["P", "_", "r", "i", "s"]
    lives = 3
    country = "France"
    show_country = True
    difficulty = 1

    from hangman_game import print_game_state
    print_game_state(display, lives, country, show_country, difficulty)
    
    captured = capfd.readouterr()
    assert "Lives: 3" in captured.out
    assert "P _ r i s" in captured.out
    assert "Guess the capital of : France" in captured.out



License

This project is licensed under the MIT License - see the LICENSE file for details.

Contributions

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

You can edit the links and add more project-specific information like your GitHub profile link, contributing guidelines, or additional sections as needed!