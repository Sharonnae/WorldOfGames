import pyfiglet
from random import randint
from utils import is_in_range
import config


def generate_number(difficulty):
    return randint(1, difficulty)


def get_guess_from_user(difficulty, guess_string):
    try:
        guess = int(input(guess_string, difficulty))
    except ValueError:
        print(config.selection_errors[1])
        return get_guess_from_user(difficulty)

    if not is_in_range(guess, 1, difficulty+1):
        return get_guess_from_user(difficulty)

    return guess


def compare_results(actual_number, guess_number):
    return actual_number == guess_number


def play(difficulty):
    print(pyfiglet.figlet_format(config.guess_game))
    result = compare_results(generate_number(difficulty), get_guess_from_user(difficulty, config.enter_a_guess))
    return result
