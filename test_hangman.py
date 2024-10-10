import pytest
from main_hangman import make_dict_from_txt, pick_random_word, update_display, is_game_lost, is_game_won

def test_make_dict_from_txt():
    """Test for funkcion wich should maka a dictionary with city:country - (key:value)"""
    test_content = "France|Paris\nCzech Republic|Prague\nUnited Kingdom|London\n"
    test_file = "test_countries_and_cities" #empty file for writing content 
    with open(test_file, "w", encoding="utf-8") as file:
        file.write(test_content)

    result = make_dict_from_txt(test_file) #Call the function for test

    expected = {"Paris": "France", "Prague": "Czech Republic", "London": "United Kingdom"} #Check to result (what should be outcome)
    assert result == expected


def test_pic_random_word():
    cities_dict = {"Paris": "France", "Prague": "Czech Republic", "London": "United Kingdom"}
    random_capital, country = pick_random_word(cities_dict)

    assert random_capital in cities_dict 
    assert country == cities_dict[random_capital]


def test_update_display():
    chosen_city  = "Paris"
    display = ["_","_","_","_","_"]
    update_display(chosen_city, display, "a")
    assert display == ["_","a","_","_","_"]


def test_is_game_lost():
    lives = 0
    assert is_game_lost(lives) == True # No lives to lefft means end of the game

    lives = 5
    assert is_game_lost(lives) == False 


def test_is_game_won():
    display = ["P","a","r","i","s"] # No uderscores means right guessed word
    assert is_game_won(display) == True


def test_is_game_won():
    display = ["P","_","r","i","s"] # Underscores on display after lives = 0 means lost game
    assert is_game_won(display) == False


def test_get_user_guess(monkeypatch):
    """Test user guess with monkeypatch to simulate user input"""
    monkeypatch.setattr("builtins.input", lambda _: "a") #Simulate a user input without user interaction, always return "a"
    from main_hangman import get_user_guess
    assert get_user_guess() == "a" #assert statement check i the value returnd by get_user_guess  is equal to "a"


def test_print_game_state(capfd):
    """Verify the print game state function has the right output"""
    #Test setup
    display = ["P","_","r","i","s"]
    lives = 3
    country = "France"
    show_country = True
    difficulty = 1

    from main_hangman import print_game_state
    print_game_state(display, lives, country,show_country, difficulty)

    captured = capfd.readouterr() #Capture standard outout and standard error stdout and stderr
    assert "Lives: 3" in captured.out #Lives left are correctly printed
    assert "P _ r i s" in captured.out #Partially guessed word is correctly printed
    assert "Guess the capital of : France" in captured.out #Verify the hint about the country is displayed(printed)