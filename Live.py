import pyfiglet
import utils
import config
from MemoryGame import play as memory_game
from GuessGame import play as guess_game
from CurrencyRouletteGame import play as currency_roulette_game


def welcome(name):
    print(pyfiglet.figlet_format(config.wog_prompt))
    print(f"Hello {name}!", config.welcome_greeting)


def load_game():
    game_selection = utils.get_selection(config.game_selection_message, 1, 4, load_game)
    if game_selection[1] != 0:
        return

    difficulty_level_selection = utils.get_selection(config.difficulty_level_message, 1, 6, load_game)
    if difficulty_level_selection[1] != 0:
        return

    utils.clear()

    if game_selection[0] == 1:
        return memory_game(difficulty_level_selection[0])

    elif game_selection[0] == 2:
        return guess_game(difficulty_level_selection[0])

    elif game_selection[0] == 3:
        return currency_roulette_game(difficulty_level_selection[0])

    else:
        raise(config.raise_errors[0])
