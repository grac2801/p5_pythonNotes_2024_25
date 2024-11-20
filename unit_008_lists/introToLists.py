'''
2024-11-18
ogracias
title = Intro to lists
'''

# imports
import random

# global variables | constants


# functions
def removeLastItemInList(L):
    '''
    list --> list
    Removes last item in my list
    removeLastItemInList([1, 2, 3)] --> [1, 2]
    '''
    del L[-1]
    return L

def removeFirstItemWithPop(passedList):
    '''
    list --> list
    removes first item in my list
    removeFirstItemWithPop([1, 2, 3]) --> [2, 3]
    '''
    passedList.pop(0)
    return passedList

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
    
    
    print('\n\n*******************')
    print('insert items to a list')
    print('*******************')
    marxes = ['Groucho', 'Chico', 'Harpo', 'Hunter', 'Mario']
    print(marxes)
    # Add new item at the start of marxes --> "first"
    marxes.insert(0, "first")
    print(marxes)
    
    
    print('\n\n*******************')
    print('Ways to delete or remove items from a list')
    print('*******************')
    marxes = ['Groucho', 'Chico', 'Harpo', 'Hunter', 'Mario']
    print(marxes)
    del marxes[0] # delete using del (index)
    print(marxes)
    
    # delete using value
    marxes.remove("Hunter")
    print(marxes)
    
    
    # remove using pop() | Default value = last value
    marxes.pop()
    print(marxes)
    
    # remove first item using pop()
    marxes.pop(0)
    print(marxes)
    
    
    print('\n\n*******************')
    print('find the index')
    print('*******************')
    marxes = ['Groucho', 'Chico', 'Harpo', 'Hunter', 'Mario']
    print(marxes)
    
    print(marxes.index('Hunter'))
    
    
    is_here = "mario" in marxes
    print(is_here)
    
    
    
    print('\n\n*******************')
    print('join()')
    print('*******************')
    marxes = ['Groucho', 'Chico', 'Harpo', 'Hunter', 'Mario']
    print(marxes)
    print(', '.join(marxes))
    
    
    friends = ['Harry', 'Hermione', 'Ron']
    print(friends)
    separator = ' & '
    joined_names = separator.join(friends)
    print(joined_names)
    
    print('\n\n*******************')
    print('sort()')
    print('*******************')
    marxes = ['Groucho', 'Chico', 'Harpo', 'Hunter', 'Mario']
    print(marxes)
    # first way --> sorts, but makes a copy of the array.
    sorted_marxes = sorted(marxes)
    marxes[0] = 'New'
    print(marxes)
    print(sorted_marxes)
    
    # sort in place | No copy is made
    marxes = ['Groucho', 'Chico', 'Harpo', 'Hunter', 'Mario']
    print(marxes)
    marxes.sort(reverse=True)
    print(marxes)
    
    
    print(len(marxes))
    
    
    print('\n\n*******************')
    print('pass a list as a  parameter to a function')
    print('*******************')
    numbers = [4, 8, 52, 4.2, 6, 45]
    print(removeLastItemInList(numbers))
    
    a = [1, 2, 3]
    print('a = ', a)
    b = a[:]
    print('b = ', b)
    a[0] = 1000
    print('a = ', a)
    print('b = ', b)
    
    #===============================================================================================
    # Make a list of 4 names, pass them as a list parameter, and remove first item using pop()
    #===============================================================================================
    listToSendToFx = ['Ella', 'Dominic', 'Guillermo', 'Ethan']
    print(removeFirstItemWithPop(listToSendToFx))
    
    
    print('\n\n*******************')
    print('min and max')
    print('*******************')
    myNumbers = [4, 8.2, 9, 6, 3.1]
    print(min(myNumbers))
    print(max(myNumbers))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
