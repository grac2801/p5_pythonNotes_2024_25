'''
2025-01-17
ogracias
title = tuple intro
'''
from encodings import idna

# imports


# global variables | constants


# functions


if __name__ == '__main__':
    fact = 'tuples are immutable'
    print('\n\n*******************')
    print('1. empty tuple')
    print('*******************')
    empty_tuple = ()
    print(empty_tuple)
    
    
    print('\n\n*******************')
    print('2. making tuples')
    print('*******************')
    friends = ('Rob', 'Nancy', "Esther")
    print(friends)
    print(type(friends))
    
    
    print('\n\n*******************')
    print('3.single item tuple')
    print('*******************')
    myTuple = 5,
    print(myTuple)
    
    print('\n\n*******************')
    print('4. unpacking a tuple')
    print('*******************')
    trees = ('cedar', 'oak', 'lemon')
    a, b, c = trees
    print(a)
    print(b)
    print(c)
    
    
    
    print('\n\n*******************')
    print('5.swapping values')
    print('*******************')
    password = 'swordfish'
    ice_cream = 'chocolate'
    print('password = ', password, ', icecream = ', ice_cream)
    password, ice_cream = ('chocolate', 'swordfish')
    print('password = ', password, ', icecream = ', ice_cream)
    
    
    
    print('\n\n*******************')
    print('6. list to tuple')
    print('*******************')
    myList = ['one', 'two', 'three']
    myTuple = tuple(myList)
    print(myTuple)
    
    #===============================================================================================
    # tuples vs lists
    # 1. tuples use less space
    # 2. can't change tuples by error
    # 3. You can use tuple as keys in a dictionary
    # 4. can be passed as parameters into a function
    #===============================================================================================
    
    myList.append('four')
    # myTuple.append('four')
    
    
    print('\n\n*******************')
    print('7. for loop and tuples')
    print('*******************')
    myTuple = ('Ram', 23, 10, 'Stephanie', 17, 'Alexa')
    myElement = 23
    for t in myTuple:
        if t == myElement:
            print('index of given element', myElement, ' is: ', myTuple.index(t))
    
    
    print('\n\n*******************')
    print('8.[i] syntax')
    print('*******************')
    for i in range(len(myTuple)):
        print(i, myTuple[i])
    
    
    # print('\n\n*******************')
    # print('9. list of tuples and using user input')
    # print('*******************')
    # studentList = []
    # numStudents = int(input('How many students? '))
    # for i in range(numStudents):
    #     fn = input('first name? ')
    #     ln = input('last name? ')
    #     idNum = input('id number? ')
    #     student_tuple = (fn, ln, idNum)
    #     studentList.append(student_tuple)
    # print(studentList)
    
    
    
    print('\n\n*******************')
    print('10. tuples into a list (zip)')
    print('*******************')
    tuple_fn = 'John', 'Mary', 'Francis'
    tuple_ln = 'Cooper', 'Armstrong', 'Pedroza'
    tuple_to_list = list(zip(tuple_fn, tuple_ln))
    print(tuple_to_list)
    
    
    
    print('\n\n*******************')
    print('11. indices and tuples')
    print('*******************')
    tuple_cities = ('San Jose', 'San Diego', 'San Francisco')
    print('The second city is:', tuple_cities[1])
    
    
    
     
    
    
    
    
    
    
    
    
