import random
from .utils import clean_input

class Player:
    def __init__(self, name, marker, is_computer=False):
        """
        Initialize a player with optional computer control
        
        Args:
            name (str): Player's name
            marker (str): 'X' or 'O'
            is_computer (bool): Whether this is a computer player
        """
        self.name = name
        self.marker = marker
        self.is_computer = is_computer
        
    def get_move(self, board):
        """Get move from human or computer player"""
        if self.is_computer:
            return self._get_computer_move(board)
        return self._get_human_move(board)
        
    def _get_human_move(self, board):
        """Get validated move input from human player"""
        available_moves = board.get_available_moves()
        prompt = f"{self.name}'s Turn ({self.marker}):\nEnter position (1-9): "
        
        while True:
            move = clean_input(input(prompt))
            if board.is_valid_move(move):
                return move
            print(f"Invalid move. Available positions: {', '.join(map(str, available_moves))}")
    
    def _get_computer_move(self, board):
        """Medium difficulty: blocks or wins if possible, otherwise random"""
        available_moves = board.get_available_moves()
        
        # First check for winning move
        for move in available_moves:
            temp_board = board.copy()
            temp_board.make_move(str(move), self.marker)
            if temp_board.check_win(self.marker):
                return str(move)
        
        # Then check for blocking move
        opponent_marker = "O" if self.marker == "X" else "X"
        for move in available_moves:
            temp_board = board.copy()
            temp_board.make_move(str(move), opponent_marker)
            if temp_board.check_win(opponent_marker):
                return str(move)
        
        # Otherwise random
        move = str(random.choice(available_moves))
        print(f"{self.name} chooses position {move}")
        return move