'''
2024-10-21
ogracias
title = count variables
'''

# imports


print('\n\n*******************')
print('#1- first counter')
print('*******************')
name = input('Enter a name: (STOP to end) ')
counter = 0

while(name != 'STOP'):
    counter += 1
    print('You entered: \u2192' + name)
    name = input('Enter a name: (STOP to end) ')

print('You entered ' + str(counter) + ' name(s)')


print('\n\n*******************')
print('#2- second counter addition')
print('*******************')
num = int(input('Enter a number: '))
total = 0

while(num != -1):
    print('You entered ' + str(num))
    total += num
    num = int(input('Enter a number: '))

print('The sum of my input numbers is', total)
    
#=================================================================================================
# Student activity:
# write a program that will prompt a suer to enter a positive
# number. while entering negative ones. Count how many times
# it takes before a positive value is input.
#=================================================================================================

n = int(input('Enter a positive number: '))
total = 1

while(n < 0):
    n = int(input('Enter a positive number: '))
    total += 1

print('That took you', total, 'tries.')
     








