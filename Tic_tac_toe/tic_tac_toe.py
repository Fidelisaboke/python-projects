from random import randrange

# Creating the board and assigning all squares with null (None)
def create_empty_board():
    empty_board=[[None for i in range(3)] for j in range(3)]
    return empty_board

# Filling the empty board
def fill_board():
    board = create_empty_board()
    square_value=1
    for row in board:
        for square in range(len(row)):
            row[square] = square_value
            square += 1
            square_value +=1
    return board


# Creating the board's interface
def display_board(board):
    print(f"""
    +-------+-------+-------+
    |       |       |       |
    |   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
    |       |       |       |
    +-------+-------+-------+
    """)

display_board(fill_board())