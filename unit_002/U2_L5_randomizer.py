'''
2024-10-09
ogracias
topic = randomizer
'''

# imports
import random

print(random.random())

#===============================================================================
# I have 2 dice and I want to get the value of both
# once they have been tossed.
#===============================================================================

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
total = die1 + die2
print(f'The total is {total}')


#===============================================================================
# More universal way to display random numbers
#===============================================================================
# * = number of items
# + = starting

print(int(random.random() * 6) + 1)


print('\n\n********************')
print('choice')
print('********************')
myFriends = ["Alex", "Patty", 'Stacey', "John"]
print(random.choice(myFriends))


#===============================================================================
# Student activity
# write a program to generate a unique password:
# number has to be between 1 - 100 included
# name of an animal from a list of 4
# number between 6 and 98
# example = 45dog37
#===============================================================================
num1 = str(random.randint(1, 100))
animal = random.choice(['dog', 'cat', 'mouse', 'ant'])
num2 = str(random.randint(6, 98))
print('pw is ' + num1 + animal + num2)






















