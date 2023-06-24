import random
from art import stages, logo
from words import word_list

"""
Retuns a word for the game,
it takes it from the imported list,
converts all user input to uppercase.
"""
def get_word():
    word = random.choice(word_list)
    return word.upper()

