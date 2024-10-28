'''
2024-10-28
ogracias
topic = calculator functions
'''

# imports
from random import randint

#functions
def add():
    firstNum = float(input('Enter a first number: '))
    secondNum = float(input('Enter a second number: '))
    total = firstNum + secondNum
    print('The result is', total)
    
    
def subtract():
    firstNum = float(input('Enter a first number: '))
    secondNum = float(input('Enter a second number: '))
    total = firstNum - secondNum
    print('The result is', total)

def flipCoin():
    outcome = randint(0, 1)
    if outcome == 1:
        print('Heads')
    else:
        print('Tails')


if __name__ == '__main__':
    print('from calculator module')
    add()






