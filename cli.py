import logging
import os
from logic import make_empty_board, get_winner, other_player, print_board, take_turn

# Setup logging
log_directory = "logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

logging.basicConfig(
    filename=os.path.join(log_directory, 'game.log'),
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def main():
    board = make_empty_board()
    winner = None
    current_player = 'X'
    
    logging.info("Game started")
    
    while winner is None:
        print_board(board)
        if take_turn(current_player, board):
            winner = get_winner(board)
            if winner is None:
                current_player = other_player(current_player)
            else:
                logging.info(f"{winner} has won the game")
        else:
            logging.warning(f"Invalid move by {current_player}")

    print_board(board)
    if winner:
        print(f"\n{winner} wins!")
    else:
        print("\nThe game is a draw.")

if __name__ == '__main__':
    main()