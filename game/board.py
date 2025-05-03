class Board:
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.cells = [str(i) for i in range(1, 10)]
        
    def display(self):
        rows = [
            " | ".join(self.cells[i:i+3]) 
            for i in range(0, 9, 3)
        ]
        return "\n---------\n".join(rows)
    
    def is_valid_move(self, position):
        try:
            pos = int(position)
            return 1 <= pos <= 9 and self.cells[pos-1] not in ["X", "O"]
        except (ValueError, IndexError):
            return False
            
    def make_move(self, position, marker):
        pos = int(position)
        self.cells[pos-1] = marker
        
    def check_win(self, marker):
        # Check rows, columns, and diagonals
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        
        for combo in winning_combinations:
            if all(self.cells[i] == marker for i in combo):
                return True
        return False
        
    def is_full(self):
        return all(cell in ["X", "O"] for cell in self.cells)
        
    def get_available_moves(self):
        return [i+1 for i, cell in enumerate(self.cells) if cell not in ["X", "O"]]