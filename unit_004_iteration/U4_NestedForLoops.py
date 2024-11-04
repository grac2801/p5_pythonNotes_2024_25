'''
2024-11-04
ogracias
title = nested for loops
'''

# imports


# global variables | constants


# functions


if __name__ == '__main__':
    # print('\n\n*******************')
    # print('Basic anatomy of a nested for loop')
    # print('*******************')
    # for outer in range(1, 4):
    #     print('outer:', outer, end=' | ')
    #     for inner in range(4, 7):
    #         print('inner', inner, end=' | ')
    #     print()
    #
    #
    # print('\n\n*******************')
    # print('compounds and elements')
    # print('*******************')
    # alkali_metals = ['Li', 'Na', 'K']
    # halogens = ['F', 'Cl']
    # for metal in alkali_metals:
    #     for halogen in halogens:
    #         print(metal + halogen)
    #     print()
    #
    # print('\n\n*******************')
    # print('width and height')
    # print('*******************')
    # rows = int(input('How many rows? '))
    # cols = int(input('How many cols? '))
    # for i in range(rows):
    #     for j in range(cols):
    #         print('* ', end = '')
    #     print()
    #

    #===============================================================================================
    # student activity:
    # Replicate the image with a nested for loop
    #===============================================================================================
    figure1 = '''
    * 
    * * 
    * * * 
    * * * * 
    * * * * *
    '''
    # print(figure1)
    for i in range(1, 6):
        for j in range(i):
            print(f'{"*":2}', end= '')
        print()

    #===========================================================================================
    # student activity:
    # now draw the following pyramid
    #===========================================================================================
    '''
    * * * * * 
    * * * * 
    * * * 
    * * 
    *
    '''
    for i in range(5, 0, -1):
        for j in range(i):
            print(f'{"*":2}', end='')
        print()




