'''
2025-02-19
ogracias
title = intro to classes - Dice
'''

# imports
from python_classes.Dice import Dice

# global variables | constants



if __name__ == '__main__':
    mrG = Dice('Mr. Gracias')
    aiden = Dice('Aiden')
    
    print(mrG.tossDice())
    mrG.printDice()
    
    print('\n\n')
    
    print(aiden.tossDice())
    aiden.printDice()
    
    mrG.compareScores(aiden)
    
    
