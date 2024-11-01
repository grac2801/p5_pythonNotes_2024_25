'''
2024-10-30
ogracias
topic = scope b
'''


# imports
from random import randint


# functions
def guessNumber():
    global attempts
    guess = int(input('Enter a number \u2192'))
    attempts += 1
    test(guess)
    
def test(num):
    global attempts
    if num > rand:
        print('Your guess is too high!')
        guessNumber()
    elif num < rand:
        print('Your guess is too low!')
        guessNumber()
    else:
        print('You guess the right number!!')
        print('It only took you', attempts, ' tries.')
        
    
        
if __name__ == '__main__':
    rand = randint(1, 100)
    print(rand)
    attempts = 0
    guessNumber()
    
    
    
    
    
    
    
    
    
    
    
    