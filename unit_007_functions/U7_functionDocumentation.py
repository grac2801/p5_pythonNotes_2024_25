'''
2024-11-06
ogracias
title = Function documentation
'''

# imports


# global variables | constants


# functions
def selectOnly_d(word) -> int:
    ''' 
    1- Returns number of letter d instances
    2- String --> int
    3-selectOnly_d('day of the dead') --> 3
    '''
    # Must input documentation in every function
    count = 0
    for i in word:
        if i == 'd':
            count += 1
    return count

if __name__ == '__main__':
    total_d = selectOnly_d('day of the dead')
    print(f'The total number of d letters: {total_d}')
    x :int = 7 # Not required to do
    print(x)
    
    
    comment = ''' 
    1- Returns number of letter d instances
              2- String --> int
    3-selectOnly_d('day of the dead') --> 3
    '''
    
    print(comment)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
