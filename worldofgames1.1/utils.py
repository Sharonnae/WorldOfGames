selection_errors = ["Wrong game selected.\nPlease try again.",
                    "Wrong difficulty level selected.\nPlease try again.",
                    "Selection is not a valid number.\nPlease try again."]


def is_in_range(value, min_val, max_val, error):
    if min_val <= value < max_val:
        return True
    print(error)
    return False


def get_selection(input_message, input_error, min_val, max_val, range_error, func):
    exit_code = 0
    try:
        selection = int(input(input_message))
    except ValueError:
        print(input_error)
        func()
        exit_code = -1
        return None, exit_code

    if not is_in_range(selection, min_val, max_val, range_error):
        print(range_error)
        func()
        exit_code = -2
        return
    return selection, exit_code




