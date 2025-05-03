from collections import namedtuple
from .utils import validate_position, get_available_moves

class Board:
    def __init__(self):
        self.WinCombination = namedtuple('WinCombination', ['indices', 'description'])
        self.win_combinations = [
            self.WinCombination([0, 1, 2], "top row"),
            self.WinCombination([3, 4, 5], "middle row"),
            self.WinCombination([6, 7, 8], "bottom row"),
            self.WinCombination([0, 3, 6], "left column"),
            self.WinCombination([1, 4, 7], "middle column"),
            self.WinCombination([2, 5, 8], "right column"),
            self.WinCombination([0, 4, 8], "main diagonal"),
            self.WinCombination([2, 4, 6], "anti-diagonal")
        ]
        self.reset()
    
    def reset(self):
        self.cells = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    def display(self):
        row1 = f" {self.cells[0]} | {self.cells[1]} | {self.cells[2]} "
        row2 = f" {self.cells[3]} | {self.cells[4]} | {self.cells[5]} "
        row3 = f" {self.cells[6]} | {self.cells[7]} | {self.cells[8]} "
        separator = "-----------"
        return f"{row1}\n{separator}\n{row2}\n{separator}\n{row3}"
    
    def is_valid_move(self, position):
        return validate_position(position, self.cells)
    
    def make_move(self, position, marker):
        pos = int(position)
        self.cells[pos-1] = marker
    
    def check_win(self, marker):
        for combo in self.win_combinations:
            if all(self.cells[i] == marker for i in combo.indices):
                return True
        return False
    
    def is_full(self):
        return all(cell in ['X', 'O'] for cell in self.cells)
    
    def get_available_moves(self):
        return get_available_moves(self.cells)
    
    def copy(self):
        """Create a deep copy of the current board"""
        new_board = Board()
        new_board.cells = self.cells.copy()
        return new_board