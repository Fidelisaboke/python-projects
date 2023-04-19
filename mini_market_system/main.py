# Stock updater system
# Made by: Fidel Agade Isaboke
# Date: 2/4/2023

import stock
from time import sleep

current_stock = {}
MARKET_MENU = 'MARKET MENU'

while True:
    
    # The menu for the program 
    print(f'{MARKET_MENU:.^20}')
    print('''Welcome to the market!
    Choose an option:
        1 - Edit stock
        2 - Exit''')
    option = input('> ')
    
    # Checking for the selected option:
    if option == '1':
        in_stock_menu = True
        while in_stock_menu:
                
            # Menu for modifying the stock
            print('''Edit the stock.
            1 - Update
            2 - Delete
            3 - View current stock
            4 - Back to menu''')
            
            stock_option = input('> ')
            if stock_option == '1':
                stock.update_stock(current_stock)
            elif stock_option == '2':
                stock.delete_item(current_stock)
            elif stock_option == '3':
                stock.display_stock(current_stock)
            elif stock_option == '4':
                in_stock_menu = False
            else:
                print('Please enter a valid option.')
    elif option == '2':
        print('Exiting program...')
        sleep(2)
        break
    else:
        print('Please select a valid option.')
        sleep(2)
        continue