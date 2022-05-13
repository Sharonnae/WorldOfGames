from os import system, name
from config import selection_errors
import requests


def is_in_range(value, min_val, max_val):
    if min_val <= value < max_val:
        return True
    print(selection_errors[0])
    return False


def get_selection(input_message, min_val, max_val, func):
    exit_code = 0
    try:
        selection = int(input(input_message))
    except ValueError:
        print(selection_errors[1])
        func()
        exit_code = -1
        return None, exit_code

    if not is_in_range(selection, min_val, max_val):
        func()
        exit_code = -2
        return None, exit_code

    return selection, exit_code


def get_currency(currency, exchange):
    url = f"https://v6.exchangerate-api.com/v6/83ce6baa371cffa478fff219/latest/{currency}"

    response = requests.get(url)
    data = response.json()
    return data["conversion_rates"][exchange]


def clear():
    # for windows
    if name == 'nt':
        system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        system('clear')
