def clean_input(user_input):
    
    return user_input.strip()

def validate_position(position, cells):
   
    if not str(position).isdigit():
        return False
        
    pos = int(position)
    if pos < 1 or pos > 9:
        return False
        
    if cells[pos-1] in ['X', 'O']:
        return False
            
    return True

def available_moves_generator(board_state):
    
    for i, cell in enumerate(board_state, 1):
        if cell not in ["X", "O"]:
            yield i

def get_available_moves(board_state):
    """Get list of all available moves"""
    return list(available_moves_generator(board_state))