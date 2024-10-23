'''
2024-10-23
ogracias
topic = for loop
'''

# imports
import random

print('\n\n********************')
print('#1 review of while loop')
print('********************')
'''
You need 3 things:
1- declare and initialize variable i.e. c = 1
2- test i.e. c < 5 ---> T or F
3- change variable c += 1 or c += 4
'''
count = 0
while(count < 5):
    print('Hello')
    count += 1

print('\n\n********************')
print('#2- for loop syntax')
print('********************')
for don in range(5):
    print('Hello')

print('\n\n********************')
print('#3- value for iterator')
print('********************')
for i in range(5):
    print(i)

print('\n\n********************')
print('#4- range variations')
print('********************')
for i in range(1, 11):
    print(str(i) + ' = ' + 'Hello')

print('\n\n********************')
print('#4- range variations with steps')
print('********************')
for i in range(2, 11, 3):
    print(str(i) + ' = ' + 'Hello')
print('\n\n********************')
print('#5- backwards')
print('********************')
for i in range(100, 9, -10):
    print(i)

#===============================================================================
# Student activity:
# simulate the toss of 2 coins 3 times (use user input),
# Count how many times you got both coins with the same value
# print your results
#===============================================================================
same_side_counter = 0
n = int(input('How many coin tosses do you want? '))
for i in range(1, n + 1):
    print('toss #', i)
    coin1 = random.randint(0,1)
    if coin1 == 0:
        side = 'heads'
    if coin1 == 1:
        side = 'tails'
    print('coin 1:', side)
    coin2 = random.randint(0,1)
    if coin2 == 0:
        side = 'heads'
    if coin2 == 1:
        side = 'tails'
    print('coin 2:', side)
    print()

    if(coin1 == coin2):
        same_side_counter += 1
print('Coins were on the same side', same_side_counter, 'time(s)')
    
print('\n\n********************')
print('#6- iterate through a string')
print('********************')
country = 'United States of America'
for letter in country:
    if letter.isupper():
        print(letter, end='')

#===============================================================================
# student activity
# Iterate through a string, select the letter 'a' in the string,
# and change it to a right arrow in another string.
#===============================================================================
orig_phrase = 'Today is a great day. Don\'t you think so?'
new_phrase = ''
orig_letter = 'a'
new_letter = '\u2192'
total_a = 0

for i in orig_phrase:
    if(i == orig_letter):
        new_phrase += new_letter
        total_a += 1
    else:
        new_phrase += i
print('original phrase:', orig_phrase)
print('New phrase:', new_phrase)
print('The total number of a letters found was', total_a)



   
    
    
    
    
    



