'''
2024-11-13
ogracias
title = Strings
'''

# imports


# global variables | constants


# functions
def _1_capitalize(fn, ln):
    '''
    capitalizes first letter of my string, and keeps lowercase format for the rest of it.
    str, str --> str
    example: _1_capitalize('oscar', 'gracias') --> Oscar Gracias
    '''
    firstName = fn.capitalize()
    lastName = ln.capitalize()
    return firstName + " " + lastName

def count():
    word = input('Enter a string: ')
    myString = input('What string are you looking for? ')
    total_count = word.count(myString, 0, len(word))
    return total_count
    


if __name__ == '__main__':
    # first = input('Enter your first name: ')
    # last = input('Enter your last name: ')
    # print(_1_capitalize(first, last))
    print('MyString is found', count(), 'times')
    
    
    
    
    
    
    
    
    
