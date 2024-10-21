'''
2024-10-21
ogracias
title = ways to end a while loop
'''

# imports
import random

# print('\n\n*******************')
# print('#1- counter or user input')
# print('*******************')
# count = 1
# while(count <= 10):
#     print(f'{count:4}: Python')
#     count += 1
#
#
# print('\n\n*******************')
# print('#2 - Ask for iteration but check with an if statement')
# print('*******************')
# counter = 0
# totalSum = 0
#
# while(counter < 5):
#     n = int(input('Enter a number: '))
#     if(n % 3 == 0):
#         print(str(n) + ' is divisible by 3')
#         totalSum += n
#     counter += 1
# print('the total sum of %3:', totalSum)


#===================================================================================================
# Student activity:
# Ask user to input numbers, -1 to stop, then get the average
# of the numbers input. 
# When printing, format answer to 2 digits after the decimal point
#===================================================================================================
# counter = 0
# addition = 0
#
# n = int(input('Enter an integer. (-1 to stop): '))
# if n == -1:
#     print('-1 input. Script will end.')
# else:
#     while(n != -1):
#         counter += 1
#         addition += n
#         n = int(input('Enter an integer. (-1 to stop): '))
#     average = (addition / counter)
#     print(f'The average is: {average:.2f}')
    
print('\n\n*******************')
print('random iteration')
print('*******************')
c = 0
clockwise_arrow = '\u21BB'
triangular_arrow = '\u27A4'
anchor = '\u2693'

while(c < 5):
    value = random.randint(0, 2)
    
    if(value == 0):
        print('clockwise_arrow:', clockwise_arrow)
        c += 1
    if(value == 1):
        print('triangular_arrow:', triangular_arrow)
        c += 1
    if(value == 2):
        print('anchor:', anchor)
        c += 1












