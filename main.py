from game import board as bd
from game import players as pls

from tools.display import show_welcome_message, show_board, show_winner, prompt_play_again, starting_screen, prompt_same_players
from tools.logger import Logger
import time

def main():
    player1 = None
    player2 = None
    game_count = 1
    
    starting_screen()
    time.sleep(1.5)
    
    while True:
        print("Tic-Tac-Toe Game")
        print("----------------\n")
        
        if player1 is None or player2 is None or not prompt_same_players():
            # Player 1 setupc
            player1_choice = input("Will Player 1 be human or computer? (h/c): ").lower()
            player1_name = input("Enter Player 1 name: ").strip() or "Player 1"
            player1 = pls.Player(player1_name, "X", is_computer=(player1_choice == 'c'))
            
            # Player 2 setup
            player2_choice = input("Will Player 2 be human or computer? (h/c): ").lower()
            player2_name = input("Enter Player 2 name: ").strip() or "Player 2"
            player2 = pls.Player(player2_name, "O", is_computer=(player2_choice == 'c'))
        
        board = bd.Board()
        logger = Logger()
        logger.log_game_start(player1, player2)
        
        show_welcome_message(player1.name, player2.name)
        current_player = player1
        
        while True:
            show_board(board)
            move = current_player.get_move(board)
            
            while not board.is_valid_move(move):
                
                move = current_player.get_move(board)
            
            board.make_move(move, current_player.marker)
            logger.log_move(current_player, move, board)
            
            if board.check_win(current_player.marker):
                show_board(board)
                show_winner(current_player.name)
                logger.log_game_result(f"{current_player.name} wins!")
                break
                
            if board.is_full():
                show_board(board)
                print("It's a draw!")
                logger.log_game_result("Draw")
                break
                
            current_player = player2 if current_player == player1 else player1
            
        if not prompt_play_again():
            print("\nThanks for playing! Goodbye!\n")
            break
            
        game_count += 1

if __name__ == "__main__":
    main()