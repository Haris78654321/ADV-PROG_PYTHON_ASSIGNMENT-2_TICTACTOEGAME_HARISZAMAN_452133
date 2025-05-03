def validate_position(position):
    """Validate if position is between 1-9"""
    try:
        pos = int(position)
        return 1 <= pos <= 9
    except ValueError:
        return False

def clean_input(user_input):
    """Clean user input by stripping whitespace"""
    return user_input.strip()

def available_moves_generator(board_state):
    """Generator that yields available moves"""
    for i, cell in enumerate(board_state, 1):
        if cell not in ["X", "O"]:
            yield i