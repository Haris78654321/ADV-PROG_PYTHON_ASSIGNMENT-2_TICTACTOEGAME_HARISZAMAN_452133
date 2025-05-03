def starting_screen():
    print('''
                                        ████████████████████████████████████████████████████████
                                        █─▄─▄─█▄─▄█─▄▄▄─███─▄─▄─██▀▄─██─▄▄▄─███─▄─▄─█─▄▄─█▄─▄▄─█
                                        ███─████─██─███▀█████─████─▀─██─███▀█████─███─██─██─▄█▀█
                                        ▀▀▄▄▄▀▀▄▄▄▀▄▄▄▄▄▀▀▀▀▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▄▀▀▀▀▄▄▄▀▀▄▄▄▄▀▄▄▄▄▄▀

                                                            ⁣⭕❕⭕❕❌
                                                            ➖➕➖➕➖
                                                            ⭕❕⁣❌❕⭕
                                                            ➖➕➖➕➖
                                                            ❌❕❌❕⭕
    ''')

def show_welcome_message(player1, player2):
    starting_screen()  # Show the fancy title screen first
    print(f"\nWelcome, {player1} and {player2}!")
    print("Current Board Layout:")
    print("1 | 2 | 3\n---\n4 | 5 | 6\n---\n7 | 8 | 9\n")

def show_board(board):
    print("\nCurrent Board:")
    print(board.display())
    print()

def show_winner(winner_name):
    print(f"\nCongratulations, {winner_name}! You win!\n")

def prompt_play_again():
    while True:
        choice = input("Would you like to play again? (yes/no): ").lower().strip()
        if choice in ["yes", "y"]:
            return True
        elif choice in ["no", "n"]:
            return False
        print("Please enter 'yes' or 'no'")