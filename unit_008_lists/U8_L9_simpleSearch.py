'''
2024-12-09
ogracias
title = simple search
'''

# imports


# global variables | constants


# functions
def search(animals, value):
    indexFound = -1
    for i in range(len(animals)):
        if(animals[i] == value):
            indexFound = i
            return indexFound
    return indexFound


if __name__ == '__main__':
    words = ['cat', 'dog', 'mouse', 'lizard', 'bird']
    animal = input('What animal are your searching for? ')
    index = search(words, animal)
    print('The value appears in index position ' + str(index) + " [-1 means not found]")
