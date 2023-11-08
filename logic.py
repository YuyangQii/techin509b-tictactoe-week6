# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]



def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    return None  # FIXME


def other_player(player):
    """Given the character for a player, returns the other player."""
    return "O" if player == 'X' else 'X' # FIXME

def print_board(board):
    for row in board:
        print(" | ".join([' ' if cell is None else cell for cell in row]))
        print("-" * 9)

def take_turn(player, board):
    print(f"\n{player}'s turn.")
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))
     # Check if the selected cell is empty
    if board[row][col] is None:

        board[row][col] = player
        return True
    else:
        print("Invalid move! Cell already taken.")
        return False
    

