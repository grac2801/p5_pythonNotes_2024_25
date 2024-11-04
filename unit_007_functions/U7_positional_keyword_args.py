'''
2024-11-04
ogracias
title = positional | keyword args
'''

# imports


# global variables | constants
DAYS_OF_THE_WEEK = 7
STARTING_SALARY = 100_000
print(f'Starting salary = ${STARTING_SALARY:,.2f}')
STARTING_SALARY += 12_000
print(f'Starting salary = ${STARTING_SALARY:,.2f}')
# speed of light = 3 x 10 ^ 8 m/s
SPEED_OF_LIGHT = 3e8
print(f'Speed of light = {SPEED_OF_LIGHT:,.2f} m/s')


# functions
def menu(drink, entree, dessert):
    print(f'drink: {drink}, entree: {entree}, and dessert: {dessert}')
    
def menuWithItems(drink, entree = 'Chicken', dessert = 'pie'):
    #Positional parameters always go first
    print(f'drink: {drink}, entree: {entree}, and dessert: {dessert}')
    
def menuWithAllItems(drink = 'Tea', entree = 'Chicken', dessert = 'pie'):
    print(f'drink: {drink}, entree: {entree}, and dessert: {dessert}')
    

if __name__ == '__main__':
    menu('sprite', 'Spaghetti', 'cheesecake')
    menuWithItems('Coke')
    menuWithAllItems()
    menuWithAllItems(dessert = 'Flan')
    
