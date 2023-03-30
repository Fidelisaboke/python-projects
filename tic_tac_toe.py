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
