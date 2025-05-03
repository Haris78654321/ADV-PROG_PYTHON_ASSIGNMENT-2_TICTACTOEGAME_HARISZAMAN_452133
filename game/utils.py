def validate_position(position,cells):
    """Validate if position is between 1-9"""
    if not position.isdigit():
            return False
        
    pos = int(position)
    if pos < 1 or pos > 9:
        return False
        
    if cells[pos-1] in ['X', 'O']:
        return False
            
    return True

def clean_input(user_input):
    """Clean user input by stripping whitespace"""
    return user_input.strip()

def available_moves_generator(board_state):
    
    for i, cell in enumerate(board_state, 1):
        if cell not in ["X", "O"]:
            yield i