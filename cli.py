1# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

import os
import logging
from datetime import datetime
from logic import make_empty_board, get_winner, other_player

# Ensure logs directory exists
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configure logging settings
log_filename = datetime.now().strftime("logs/game_%Y%m%d_%H%M%S.log")
logging.basicConfig(filename=log_filename, level=logging.INFO)
# Reminder to check all the tests

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    player = "X"
    while winner == None:
        print("TODO: take a turn!")
        # TODO: Show the board to the user.
        print (board)

        # TODO: Input a move from the player.
        x, y = input("Enter the position of (x,y), split with comma: ").split(",")

        # TODO: Update the board.
        board[int(x)][int(y)] = player
        define_winner = get_winner(board)

        # TODO: Update who's turn it is.
        if not winner:
            player = other_player(player)

        print(winner)