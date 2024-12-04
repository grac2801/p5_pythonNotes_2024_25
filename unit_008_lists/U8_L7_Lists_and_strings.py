'''
2024-12-04
ogracias
title = Lists and strings
'''

# imports


# global variables | constants


# functions


if __name__ == '__main__':
    # All strings have an index value
    month = 'October'
    for i in range(len(month)):
        print(month[i])
        
    for i in month:
        print(i)
        
        
    # You can also replace values in the array, but YOU HAVE TO USE INDICES
    print('\n')
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    print('original weekdays', weekdays)
    
    for i in range(len(weekdays)):
        weekdays[i] = weekdays[i].replace("day", "") 
    print('modified weekdays', weekdays)
    

    # parallel processing | parallel lists
    name = ['Alice', 'Bob', 'Carl']
    color = ['blue', 'orange', 'red']
    age = [16, 15, 17]

    for i in range(len(name)):
        print(name[i] + ' is ' + str(age[i]) + ' years old')
        print('His/her favorite color is: ' + color[i])
        print()


    # zip()
    names = ['Alice', 'Bob', 'Carl']
    scores = [98, 97, 99]
    result = zip(names, scores)
    print(list(result))



    print(ord('A'))
    print(chr(65))










