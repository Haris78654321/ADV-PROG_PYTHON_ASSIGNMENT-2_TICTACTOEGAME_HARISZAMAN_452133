from pathlib import Path
from datetime import datetime

class Logger:
    def __init__(self):
        self.move_count = 0
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.log_dir = Path("game_log") / f"game_{timestamp}"
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.log_file = self.log_dir / "log.txt"
        
    def log_game_start(self, player1, player2):
        with open(self.log_file, "w") as f:
            f.write(f"Game started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Player 1: {player1.name} ({player1.marker})\n")
            f.write(f"Player 2: {player2.name} ({player2.marker})\n\n")
            f.write("Move History:\n")
            
    def log_move(self, player, move, board):
        self.move_count += 1
        with open(self.log_file, "a") as f:
            f.write(f"\nMove {self.move_count}: {player.name} ({player.marker}) -> Position {move}\n")
            f.write("Current Board:\n")
            f.write(board.display() + "\n")
            
    def log_game_result(self, result):
        with open(self.log_file, "a") as f:
            f.write(f"\nGame ended at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Final Result: {result}\n")