'''
2024-10-18
ogracias
topic = while loop
'''

# imports
import random

print('\n\n********************')
print('#1 basic while loop')
print('********************')
#===============================================================================
# a) first step = to declare and initalize a variable
# b) second step = test
# c) third step = change variable
#===============================================================================
# num = 0
# while num < 5:
#     print('num < 5')
#     num += 1
# print('Done')


print('\n\n********************')
print('#2 The sentinel value')
print('********************')
# number = int(input('Enter a number, -1 to stop'))
# while(number != -1):
#     print('You entered: ' + str(number))
#     number = int(input('Enter a number, -1 to stop'))
# print('Done entering numbers')
    
print('\n\n********************')
print('#3 Asking for a name.')
print('********************')
# name = input('Enter a name: ')
# while name != 'Ada':
#     print(name + ' is an interesting name')
#     name = input('Enter a name: ')
# print('Great, my name is also Ada')
    

#===============================================================================
# student activity:
# Using a while loop, come up with 10 random values from 
# 30-40 inclusive, and print them out.
#===============================================================================
counter = 1
#Let's add all the random numbers
total = 0
while(counter <= 10):
    random_number = random.randint(30, 40)
    total += random_number
    print('Number selected: ' + str(random_number))
    counter += 1
print('The total sum for all numbers is: ' + str(total))














