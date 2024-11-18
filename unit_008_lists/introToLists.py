'''
2024-11-18
ogracias
title = Intro to lists
'''

# imports
import random

# global variables | constants


# functions


if __name__ == '__main__':
    print('\n\n*******************')
    print('How to make a list (2 ways)')
    print('*******************')
    # Empty list
    myList = []
    print('Empty list', myList)
    
    otherList = list()
    print('otherList', otherList)
    
    # make a list and populate it with values
    values = list()
    print(values)
    for i in range(10):
        myRandonNum = random.randint(1, 10)
        values.append(myRandonNum)
    print(values)
    
    weekdays = ['Mon', 'Tue', 'Wed', 'Thu']
    print(weekdays)
    big_birds = ['Emu', 'Ostrich', 'Cassowary']
    first_names = ['Guillermo', 'Adan', 'Giovanni']
    combined = [weekdays, big_birds, first_names]
    
    print('combined arrays:', combined)
    # only big_birds
    print('birds only:', combined[1])
    
    # Cassowary bird only
    print('cassowary index:', combined[1][2])
    
    
    print('\n\n*******************')
    print('offsets | slices')
    print('*******************')
    marxes = ['Groucho', 'Chico', 'Harpo', 'Hunter', 'Mario']
    # 3 set values
    # 1st value = beginning, 2nd value = end(exclusive), 3rd value = step
    print(marxes[0: 5: 1])
    print(marxes[::])
    print(marxes[::2])
    
    # slice
    # I want all items in array except last one
    print(marxes[:4:])
    # print last 4 only
    print(marxes[1::])
    
    # print last item
    print(marxes[-1])
    
    # list all items backwards
    print(marxes[-1::-1])
    
    
    print('\n\n*******************')
    print('change items in my list')
    print('*******************')
    marxes = ['Groucho', 'Chico', 'Harpo', 'Hunter', 'Mario']
    print(marxes)
    
    # replace Harpo for Daniel
    marxes[2] = 'Daniel'
    print(marxes)
    
    
    print('\n\n*******************')
    print('append() and extend')
    print('*******************')
    marxes = ['Groucho', 'Chico', 'Harpo', 'Hunter', 'Mario']
    print(marxes)
    extended_names = ['Brie', 'Alexa']
    print(extended_names)
    
    # append
    marxes.append(extended_names)
    print(marxes)
    
    marxes = ['Groucho', 'Chico', 'Harpo', 'Hunter', 'Mario']
    print(marxes)
    extended_names = ['Brie', 'Alexa']
    print(extended_names)
    # extended
    marxes.extend(extended_names)
    print(marxes)
    
    
    print('\n\n*******************')
    print('+=')
    print('*******************')
    marxes = ['Groucho', 'Chico', 'Harpo', 'Hunter', 'Mario']
    print(marxes)
    others = ['Ella', 'Christina']
    marxes += others
    print(marxes) # extend and += do the same job
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
