import random
import os

from art import stages, logo
from words import word_list
from countries import country_list
from food_and_drink import fd_list


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
    
    word = ""
    print(logo)
    name = input("Please enter your name: ").capitalize()
    print("\n")
    print(f"Welcome to the game, {name}!")
    print("\n")
    

    while True:
        category = select_category()

        decision = input(f"{name}, you have 6 lives and have selected {category}. \nAre you happy with your choice? (Y/N) ").upper()

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
            selection = int(input("\nPlease select a category:\n1. Countries\n2. Food\n3. General\n\n"))
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

#Welcome messages
    print(logo)
    print("Let's start playing!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                print("You have", (tries -1), "attempts left.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def display_hangman(tries):
    """
    Gets the hangman stages,
    and it displays it.
    """ 
    return stages[tries]


def main():
    """
    Main function: it gets a word and pass it to play,
    Ask the user input for playing again or not,
    """
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()