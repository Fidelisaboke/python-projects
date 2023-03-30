#Main program to execute the functions in the tictactoe module
import tictactoe
from time import sleep

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

while True:
    option = input("> ")

    if option == '1':
        while not game_over:
            print("Waiting for computer...")
            tictactoe.draw_move(board)
            sleep(2)
            tictactoe.display_board(board)
            tictactoe.enter_move(board)
            sleep(1)
            tictactoe.display_board(board)
            remaining_options = tictactoe.make_list_of_free_fields(board)
            
            cpu_winner = tictactoe.victory_for(board, 'X')
            player_winner = tictactoe.victory_for(board, 'O')
            
            if remaining_options == []:
                print("It is a draw! Good game!")
                game_over = True
                break
            elif cpu_winner:
                print('Computer wins!')
                game_over = True
                break
            elif player_winner:
                print('Player wins!')
                game_over = True
                break

    elif option == '2':
        print('Closing program...')
        sleep(1)
        break
    else:
        print("Enter a valid option.")