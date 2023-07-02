import gspread
from google.oauth2.service_account import Credentials

import random
import os
import sys

from art import stages, logo, game_over, leaderboard_heading, end_line
from words import word_list
from countries import country_list
from food_and_drink import fd_list

# API CONSTS
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman_leaderboard')

leaderboard = SHEET.worksheet("leaderboard")

data = leaderboard.get_all_values()

# SCORECOUNTER CONSTS
CORRECT_GUESSED = 25
FULL_WORD_SCORE = 200

GAME_SELECT ="""Please select an option:\n
1 - Play again\n
2 - Leaderboard\n
3 - Exit game\n"""


def clear():
    """
    Clears the screen
    """

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def welcome_player():
    """
    Welcomes the user, asks to select a category and
    checks whether they are happy with their decision
    """
    global name
    print(logo)
    while True:
        name = input("Please enter your name: ").capitalize()
        print("\n")

        # Ensures that the user enters a name and this is not left blank
        if len(name) == 0:
            print("This is not a valid name!")
            continue
        else:
            break

    print(f"Welcome to the game, {name}!")

    # Starts scores at value 0
    score = 0

    while True:
        category = select_category()

        decision = input(f"{name}, you have 6 lives "
                         f"and have selected: {category}.\n"
                         "Are you happy with your choice? (Y/N)\n").upper()

        if decision == "Y":
            print("Let's play. Good luck!\n")
            break
        elif decision == "N":
            clear()
            print(logo)
        else:
            print("Invalid input. Please enter 'Y' or 'N'.\n")

    return category


def select_category():
    """
    Prompts the user to select a category from a list.
    """

    while True:
        try:
            selection = int(input("\nPlease select a category: \n"
                            "1. Countries\n2. Food\n3. General\n\n"))
            if 1 <= selection <= 3:
                break
            else:
                print("Invalid entry. Please select a valid category.\n")
        except ValueError:
            print("Please enter a number between 1 and 3.\n")

    if selection == 1:
        category = "Countries"
    elif selection == 2:
        category = "Food"
    else:
        category = "General"

    return category


chosen_category = welcome_player()

# Clear screen for better user visibility
clear()

word = ""


def get_word():

    """
    Returns a random word based on the category selected,
    it takes it from the imported list,
    converts all user input to uppercase.
    """

    if chosen_category == "Countries":
        word = random.choice(country_list)
        return word.upper()
    elif chosen_category == "Food":
        word = random.choice(fd_list)
        return word.upper()
    else:
        word = random.choice(word_list)
        return word.upper()


def play(word):
    """
    This function runs the game:
    Define variables, welcome the user to the game,
    the while loop displays a word to guess while this is not guessed,
    if the user inputs an already guessed letter it gives feedback,
    also if the user enters a wrong answer,
    otherwise the user gets positive feedback from guessing the word.
    """
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    score = 0

# Welcome messages
    print(logo)
    print("Let's start playing!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    # While the word is not guessed and the player still has tries left
    while not guessed and tries > 0:
        display_score(score)

        guess = input("Please guess a letter or word: \n").upper()
        if len(guess) == 1 and guess.isalpha():

            # Letter guessed repeated
            if guess in guessed_letters:
                print("You already guessed the letter", guess)

            # Letter guessed NOT in the word
            elif guess not in word:
                print(guess, "is not in the word.")
                print("You have", (tries - 1), "attempts left.")
                tries -= 1
                guessed_letters.append(guess)

            # Letter guessed in the word
            else:
                print("Good job,", guess, "is in the word!")
                score += CORRECT_GUESSED

                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i,
                           letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True

        # Player guesses the FULL word
        elif len(guess) == len(word) and guess.isalpha():
            # The word guessed has been entered again
            if guess in guessed_words:
                print("You already guessed the word", guess)
            # The word guessed is not the right guess
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        # Unsupported guesses
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    # Player WINS
    if guessed:
        print("Congrats, you guessed the word! You win!\n")
        # Adds extra score if the full word is guessed
        score = score + FULL_WORD_SCORE

    # Player LOSES
    else:
        display_name(name)
        display_score(score)

        print("Sorry, you ran out of tries."
              "The word was " + word + ". Maybe next time!\n")
        print(game_over)

    update_worksheet(score)
    
   


def display_hangman(tries):
    """
    Gets the hangman stages,
    and it displays it
    """
    return stages[tries]


def display_name(name):
    """
    Display player name
    """

    print(f"NAME: {name}\n")


def display_score(score):
    """
    Display player score during the game
    """

    print(f"SCORE: {score}\n")


def update_worksheet(score):
    """
    Update a new row in the Hangman worksheet
    This updates a new row with the name and score.
    """

    print("Updating Leaderboard...\n")
    worksheet_to_update = SHEET.worksheet("leaderboard")

    worksheet_to_update.append_row([str(name[0:7]), score])
    print("\n")
    print("Leaderboard updated successfully.\n")


def display_leaderboard():
    """
    Displays to the players the 10 best scores
    """

    print(leaderboard_heading)
    score_sheet = SHEET.worksheet("leaderboard").get_all_values()[1:]
    for data in score_sheet:
        data[1] = (data[1])

    update_data = sorted(score_sheet, key=lambda x: int(x[1]), reverse=True)

    if (len(update_data) < 10):
        count = len(update_data)
    else:
        count = 10

    for i in range(0, count):
        print(f"""
        {i+1}\t{update_data[i][0]}\t  {update_data[i][1]}""")
    print(end_line)
    print("\n")

def exit_program():
    """
    Function to exit the game
    """
    print(f"\n\tThanks for playing, {name}.\n")
    print(f"\n\tExiting the game..")
    sys.exit(0)

def main():
    """
    Main function: it gets a word and pass it to play,
    When finishing the game asks the user input for:
    1 - Play again
    2 - Leaderboard
    3 - Exit game
    """
    play_game = True
    while True:
        if play_game:
            word = get_word()
            play(word)

        user_input = input(f"{GAME_SELECT}").upper()
        if user_input == "1":
            print(f"\n\tYou have selected to continue playing.\n")
            play_game = True
        elif user_input == "2":
            display_leaderboard()
            play_game = False
        elif user_input == "3":
            exit_program()
        else:
            print(f"""\n\t
            That is not a valid option. Please try again.\n""")
            play_game = False


if __name__ == "__main__":
    main()
