import utils


def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.\n")


def load_game():
    game_selection_message = "Please choose a game to play:\n" \
                             "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess " \
                             "it back.\n"\
                             "2. Guess Game - guess a number and see if you chose like the computer.\n" \
                             "3. Currency Roulette - try and guess the value of a random amount of USD in ILS.\n"

    difficulty_level_message = "Please choose game difficulty from 1 to 5:"

    game_selection = utils.get_selection(game_selection_message, utils.selection_errors[2], 1, 4,
                                           utils.selection_errors[0], load_game)
    if game_selection[1] != 0:
        return
    difficulty_level_selection = utils.get_selection(difficulty_level_message, utils.selection_errors[2], 1, 6,
                                                       utils.selection_errors[1], load_game)
    if game_selection[1] != 0:
        return

    return game_selection[0], difficulty_level_selection[0]


