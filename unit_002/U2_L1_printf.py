'''
2024-09-16
ogracias
title = special formatting
'''
print('*******************')
print('data types in printf')
print('*******************')
'''
s -> String
d -> integer. Use comma as a separator
e -> exponents
f -> float or fixed point notation. [Default is 6]
'''
variable = 1045634
print(f'Using numeric {variable}')
print(f'Using numeric {variable = }')
print(f'Using numeric {variable:d}') 
print(f'Using numeric {variable:10}') 
print(f'Using numeric {variable:e}') 

print('\n\n*******************')
print('float variables')
print('*******************')
pi = 3.141592653589793
print(f'Using the value of pi = {pi}')
print(f'|{pi:<10}|')
print(f'|{pi:>10}|')
print(f'|{pi:^10}|')
print(f'|{pi:10}|')

floatVariable = 1045634.9854564545
print(f'This prints without formatting {floatVariable = }')
print(f'This prints without formatting {floatVariable}')
print(f'This prints without formatting {floatVariable:f}')
print(f'This prints without formatting {floatVariable:,f}')
print(f'This prints without formatting {floatVariable:,.2f}')
print(f'This prints without formatting {floatVariable:+,.2f}')

print('\n\n*******************')
print('Strings')
print('*******************')
version = 'Python 3.12'
print(f'|{version:10}|')
print(f'|{version:<10}|')
print(f'|{version:>10}|')
print(f'|{version:^10}|')

print('\n\n*******************')
print('tabbing')
print('*******************')
first = 'Monday'
second = "Tuesday"
third = 'Wednesday'
meal1 = 'fish'
meal2 = 'soup'
meal3 = 'beef'
print(f'|{first:10s}{second:10s}{third:10s}|')
print(f'|{meal1:10s}{meal2:10s}{meal3:10s}|')



