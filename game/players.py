class Player:
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker
        
    def get_move(self, board):
        available_moves = board.get_available_moves()
        prompt = f"{self.name}'s Turn ({self.marker}):\nEnter a position (1-9): "
        
        while True:
            try:
                move = input(prompt).strip()
                if move.isdigit() and int(move) in available_moves:
                    return move
                print(f"Invalid move. Available positions: {', '.join(map(str, available_moves))}")
            except ValueError:
                print("Please enter a number between 1 and 9")