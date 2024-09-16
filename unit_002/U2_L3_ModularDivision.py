'''
2024-09-16
ogracias
title = Modulus or mod (remainder)
'''

print('\n\n*******************')
print('modular division')
print('*******************')
#===================================================================================================
# Modulus is used for remainders, patters, cybersecurity hash values, even or odds.
#===================================================================================================
print('When 10 is divided by 3, the remainder is', 10 % 3)
'''
When the first value is < the second value, the answer is the first value.
'''
firstValue = int(input('Enter first value: '))
secondValue = int(input('Enter second value: '))
print('the remainder is:', firstValue % secondValue)

print('\n\n*******************')
print('hours, minutes')
print('*******************')
totalMinutes = int(input('How many minutes are you converting? '))
hours = int(totalMinutes / 60)
minutesRemaining = totalMinutes % 60
print(f'There are {hours:d} hour(s) and {minutesRemaining:d} minute(s) in {totalMinutes:d} minutes')

print(f'Question 1')
print('a)', '9 -3 = ', (9-3))


