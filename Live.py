import pyfiglet
import utils
import config
from MemoryGame import play as memory_game
from GuessGame import play as guess_game
from CurrencyRouletteGame import play as currency_roulette_game
from Score import update_score_file


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
        score = memory_game(difficulty_level_selection[0])

    elif game_selection[0] == 2:
        score = guess_game(difficulty_level_selection[0])

    elif game_selection[0] == 3:
        score = currency_roulette_game(difficulty_level_selection[0])

    else:
        raise(config.raise_errors[0])

    if score is True:
        update_score_file(difficulty_level_selection[0])
