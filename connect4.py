import numpy as np
def create_board():
    board = np.zeros((6,7))
    return board
def drop_piece():
    pass

def is_valid_location(board, col):
    return board[5][col] == 0

def get_next_open_row():
    pass

board = create_board()
print(board)
game_over = False
turn = 0

while not game_over:
    # ask for player 1 input
    if turn == 0:
        col = int(input("Player 1 Make your selection (0-6):"))
        

    
    #ask for player 2 input
    else:
        col = int(input("Player 2 Make your selection (0-6):"))
        
    turn += 1
    turn = turn % 2