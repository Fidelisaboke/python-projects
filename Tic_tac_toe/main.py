# Written by: Fidel Agade Isaboke
# Idea adopted from: Cisco Skills for All
# Main program to execute the functions in the tictactoe module
import tictactoe
from time import sleep

# Function to check remaining options
def no_remaining_options(board):
    if tictactoe.make_list_of_free_fields(board) == []:
        print("It is a draw! Good game!")
        global game_over
        game_over = True
        return True
    else:
        return False


# Creating the board:
board = tictactoe.fill_board()

# Welcome message:
print("""
Welcome to the tic-tac-toe game!
Choose the following options:
1 - Play
2 - Exit
""")

game_over = False

# Creating an infinite loop to run the main statements of the program until an 'exit' condition is triggered:
while True:
    option = input("> ") # Input pointer
    if option == '1': # 'Play' option
        while not game_over: # The game will continue until the game_over condition is true.

            # 'Wait' for the computer to 'think' and make a move:
            print("Waiting for computer...")
            tictactoe.draw_move(board)
            sleep(2)

            # If there are no remaining options for the player, call the game a 'draw':
            if no_remaining_options(board):
                break

            tictactoe.display_board(board) # Display the board once the computer makes its mark, 'X'
            tictactoe.enter_move(board) # The player's turn to make a move
            sleep(1)
            tictactoe.display_board(board) # Display the board once the player makes a move
            
            cpu_winner = tictactoe.victory_for(board, 'X')
            player_winner = tictactoe.victory_for(board, 'O')
            
            # If there are no remaining options for the computer, call the game a 'draw':
            if no_remaining_options(board):
                break

            # Announce the winner if there's one:
            elif cpu_winner:
                print('Computer wins!')
                game_over = True
                break
            elif player_winner:
                print('Player wins!')
                game_over = True
                break

    elif option == '2': # 'Exit' option
        print('Closing program...')
        sleep(1)
        break
    else:
        print("Enter a valid option.")