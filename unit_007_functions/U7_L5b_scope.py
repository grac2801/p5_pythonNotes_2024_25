'''
2024-10-30
ogracias
topic = scope b
'''


# imports
from random import randint


# functions
def guessNumber():
    guess = int(input('Enter a number \u2192'))
    test(guess)
    
def test(num):
    if num > rand:
        print('Your guess is too high!')
        guessNumber()
    elif num < rand:
        print('Your guess is too low!')
        guessNumber()
    else:
        print('You guess the right number!!')
        
    
        
if __name__ == '__main__':
    rand = randint(1, 100)
    print(rand)
    guessNumber()
    
    
    
    
    
    
    
    
    
    
    
    