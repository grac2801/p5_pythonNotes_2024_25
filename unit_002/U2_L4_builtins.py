'''
2024-10-09
ogracias
topic = builtins
'''

# imports
import math
from math import sqrt
import platform


print('********************')
print('min and max')
print('********************')
myNums = [4, 5, 9, 23, 54, -3, -2]
print(max(myNums))
print(min(myNums))

friends = ['Alexa', 'Aiden', 'Ella', 'Chinh']
print(max(friends))
print(min(friends))

print('\n\n********************')
print('builtins using input')
print('********************')
# a = int(input('Enter the first number: '))
# b = int(input('Enter the second number: '))
# c = int(input('Enter the third number: '))
#
# print('The biggest value is: ' + str(max(a, b, c)))
# print('The biggest value is: ' + str(min(a, b, c)))


#===============================================================================
# student activity:
# myList = [4, 6, 2, 78, 23, 56, 12]
# print using f formatting the difference between the 
# max and min values of the list.
#===============================================================================
myList = [4, 6, 2, 78, 23, 56, 12]
print(f'The difference is {max(myList) - min(myList)}')


print('\n\n********************')
print('Using python libraries')
print('********************')
print(int(81**(1/2)))
print(int(math.sqrt(81)))# much more explicit
print((int(sqrt(81))))
print(int(math.pow(81, (1/2))))



print('\n\n********************')
print('platform module')
print('********************')
print('My current python version ' + platform.python_version())
print('My current processor is ' + platform.processor())






































