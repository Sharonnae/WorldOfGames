from pathlib import Path
from utils import SCORES_FILE_NAME, BAD_RETURN_CODE


def calculate_points(difficulty):
    return (difficulty * 3) + 5


def read_score():
    file = Path(SCORES_FILE_NAME)
    file.touch(exist_ok=True)
    with open(SCORES_FILE_NAME, "r") as score_file:
        points = score_file.read()
        if points == '':
            return 0
        elif int(float(points)) >= 0:
            return int(float(points))
        else:
            return BAD_RETURN_CODE


def update_score_file(difficulty):
    points = read_score()
    if points != BAD_RETURN_CODE:
        points += calculate_points(difficulty)
        with open(SCORES_FILE_NAME, "w") as score_file:
            score_file.write(str(points))
    else:
        print("Failed to read score, new points will not be added")
