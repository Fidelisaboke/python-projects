# Stock updater system
# Made by: Fidel Agade Isaboke
# Date: 2/4/2023

# FUNCTIONS
# getting the stock
def get_stock(stock):
    return stock
    
# viewing the stok items
def display_stock(stock):
    print(f"Current stock {stock}")
    
# updating the stock
def update_stock(stock):
    try:
        item_name = input('Enter the name of the item: ')
        item_price = float(input('Enter the item price: '))
    
        stock.update({item_name: item_price})
        display_stock(stock)
    except:
        print('An error has occured. Please check your input')

# deleting an item from the stock
def delete_item(stock):
    try:
        item_name = input('Enter the item name (as it appears in the stock): ')
        
        del stock[item_name]
        display_stock(stock)
    except:
        print('An error has occured. Try again.')
        
    