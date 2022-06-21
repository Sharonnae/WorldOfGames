from random import randint
import pyfiglet
from utils import get_currency
import config


# for given difficulty d, and total value of money t the interval will be: (t - (5 - d), t + (5 - d))
def get_money_interval(d, t):
    return t - (5 - d), t + (5 - d)


# Bug - need to add input validation\ error handling.
def get_guess_from_user(usd):
    return float(input(f"The amount is {usd} USD.\nPlease enter a guess for the ILS value"))


def calculate_usd_to_ils(usd, ils_currency):
    return usd * ils_currency


def play(difficulty):
    print(pyfiglet.figlet_format(config.guess_game))

    usd_amount = randint(1, 100)
    ils_currency = get_currency("USD", "ILS")
    ils_amount = calculate_usd_to_ils(usd_amount, ils_currency)

    interval = list(get_money_interval(difficulty, ils_amount))
    guess = get_guess_from_user(usd_amount)
    # bug - calculation is wrong. need to debug.
    return interval[0]<=guess<=interval[1]
