'''
2025-02-03
ogracias
title = boolean and not or gates
'''

# imports


# global variables | constants
canVote = False

# functions
def voting(age):
    over18 = age
    if over18 >= 18:
        canVote = True
        return canVote
    else:
        canVote = False
        return canVote

if __name__ == '__main__':
    
    #False
    print(bool(0))
    print(bool(0.0))
    print(bool(0j))
    
    #True
    print(bool(1))
    print(bool(-1))
    print(bool(1j))
    
    print('\n\n*******************')
    print('Strings')
    print('*******************')
    print(bool('True'))
    print(bool('False'))
    print(bool(''))
    print(bool(' '))
    
    print('\n\n*******************')
    print('data structures')
    print('*******************')
    print(bool([]))
    print(bool([1, 2]))
    print(bool({}))
    print(bool(None))
    
    
    print('\n\n*******************')
    print('Using in algorithm')
    print('*******************')
    myList = [1, 2, 3]
    if bool(myList):
        print('My list has some values')
        
        
    a = 5
    b = 5
    if(a - b):
        print('a and c are not equal')
    
    
    print('\n\n*******************')
    print('Logic gates')
    print('*******************')
    # OR gate
    print(False or False)
    print(False or True)
    print(True or False)
    print(True or True)
    
    print("\n\nAND gate")
    print(False and False)
    print(False and True)
    print(True and False)
    print(True and True)
    
    print("\n\nNOT gate")
    print(not True)
    print(not False)
    
    print('\n\n*******************')
    print('another example')
    print('*******************')
    weatherIsNice = False
    haveUmbrella = True
    
    if not haveUmbrella or weatherIsNice:
        print('Stay inside')
    else:
        print('Go for a walk')
    
    print('\n\n*******************')
    print("DeMorgan's law")
    print('*******************')
    weatherIsNice = True
    haveUmbrella = False
    if not (haveUmbrella or weatherIsNice):
        print('Stay inside')
    else:
        print('Go for a walk')
        
    # Apply DeMorgan's law
    if (not haveUmbrella) and (not weatherIsNice):
        print('Stay inside')
    else:
        print('Go for a walk')
        
    
    print(voting(5))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
