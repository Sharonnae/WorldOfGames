import pyfiglet
import time
from random import randint
import config
from utils import clear


def generate_sequence(difficulty):
    generated_list = []
    for i in range(difficulty):
        generated_list.append(int(randint(1, 101)))
    print(generated_list)
    time.sleep(0.7)
    clear()
    return generated_list


def get_list_from_user(difficulty):
    user_list = []
    for i in range(difficulty):
 ### bug to fix - if user enters a string it will fail.
        user_list.append(int(input(f"Enter number {i+1}:")))
    return user_list


def is_list_equal(list1, list2):
    return list1 == list2


def play(difficulty):
    print(pyfiglet.figlet_format(config.memory_game))
    input(config.enter)
    generated = generate_sequence(difficulty)
    user_guess = get_list_from_user(difficulty)
    return is_list_equal(generated, user_guess)
