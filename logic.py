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

    # Check rows
    for row in board:
        if len(set(row)) == 1 and row[0] != ' ':
            return f"{row[0]}"

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return f"{board[0][col]}"

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return f"{board[0][0]}"
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return f"{board[0][2]}"

    # Check for draw or ongoing game
    for row in board:
        for cell in row:
            if cell == ' ':
                return None



def other_player(player):
    """Given the character for a player, returns the other player."""
    
    if player == "X":
        return "O"
    elif player == "O":
        return "X"