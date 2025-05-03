from game import board as bd
from game import players as pls
from tools.display import show_welcome_message, show_board, show_winner, prompt_play_again, starting_screen
from tools.logger import Logger
import time


def main():
    while True:
        # Show starting screen with a brief pause
       
        starting_screen()
        time.sleep(1.5)
        
        
        print("Tic-Tac-Toe Game")
        print("----------------\n")
        
        # Setup players
        player1_name = input("Please enter Player 1 name: ").strip() or "Player 1"
        player2_name = input("Please enter Player 2 name: ").strip() or "Player 2"
        
        player1 = pls.Player(player1_name, "X")
        player2 = pls.Player(player2_name, "O")
        current_player = player1
        
        # Initialize game components
        board = bd.Board()
        logger = Logger()
        logger.log_game_start(player1, player2)
        
     
        show_welcome_message(player1_name, player2_name)
        
        # Game loop
        while True:
            show_board(board)
            
            # Get and validate move
            move = current_player.get_move(board)
            while not board.is_valid_move(move):
                print("Invalid move. Please try again.")
                move = current_player.get_move(board)
            
            # Make move and log it
            board.make_move(move, current_player.marker)
            logger.log_move(current_player, move, board)
            
            # Check for win or draw
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
                
            # Switch players
            current_player = player2 if current_player == player1 else player1
            
        
        # Ask to play again
        if not prompt_play_again():
           
            print("\nThanks for playing! Goodbye!\n")
            break

if __name__ == "__main__":
    main()