from random import randrange
# Creating a tuple of the two signs, ('X' and 'O'):
game_signs = ('X', 'O')

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

# Function that handles the moves of the user
def enter_move(board):
        move_done = False
        while True:
            try:
                move = int(input("Select a square to make a move: "))
                if move < 1 or move > 9:
                    print("Incorrect option. Try again.")
                else:
                    for row in board:
                        for square in range(len(row)):
                               if row[square] == move and row[square] not in game_signs:
                                row[square] = 'O'
                                move_done = True

                                if move_done:
                                    print("Move made successfully")
                                    return
            except ValueError:
                print("Integers only!")
            except TypeError:
                print("Please enter an integer.")
            except:
                print("An unknown error has occured.")


# Function that handles the moves of the computer
def draw_move(board):
    for row in board:
        for square in range(len(row)):
            if row[square] == 5:
                row[square] = 'X'
                return
    while True:
        move = randrange(1, 10)
        for row in board:
            for square in range(len(row)):
                if row[square] == move and row[square] not in game_signs:
                    row[square] = 'X'
                    return

# Producing a list of free_fields:
def make_list_of_free_fields(board):
    free_squares = []
    for row in board:
        for square in range(len(row)):
            if row[square] not in game_signs:
                free_squares.append(row[square])
    return free_squares


# Checking for a victory:
def victory_for(board, sign):
    # Specifying win conditions:
    left_diagonal_triple = [board[0][0], board[1][1], board[2][2]]
    right_diagonal_triple = [board[0][2], board[1][1], board[2][0]]
    left_triple = [board[0][0], board[1][0], board[2][0]]
    middle_triple = [board[0][1], board[1][1], board[2][1]]
    right_triple = [board[0][2], board[1][2], board[2][2]]

    # Checking a row for 3 sign elements
    for row in board:
        if all(square == sign for square in row):
            return True
        
    # Checking if a column or diagonal contains three sign elements and returns True if a win condition is met.
    # If no win conditions are met, the function returns False.
    if any(all(square == sign for square in triple) for triple in 
           [left_diagonal_triple, right_diagonal_triple, left_triple, middle_triple, right_triple]
           ):
        return True
    else:
        return False