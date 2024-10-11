'''
2024-10-11
ogracias
topic = simple if
'''

# imports
value = int(input('Enter a number: '))
if value > 0:
    print('positive')
print('Done')

print('\n\n********************')
print('use of booleans')
print('********************')
sunny = True

if sunny:
    print('I don\'t need an umbrella.')
if not sunny:
    print('I DO need an umbrella.')    
    
    
print('\n\n********************')
print('relational operators')
print('********************')
print('>', 'greater than')
print('>=', 'greater than or equal to')
print('<', 'less than')
print('<=', 'less than or equal to')
print('==', 'equal to')
print('!=', 'not equal to')
print('in', 'membership')

word = input('Enter the secret code: ')
if word == 'python':
    print('correct')


print('\n\n********************')
print('odd or even')
print('********************')
number = int(input('Enter a number: '))
if number % 2 == 0:
    print(str(number) + ' is even')
if number % 2 == 1:
    print(str(number) + ' is odd')

      
print('\n\n********************')
print('membership')
print('********************')
friends = ['Alex', 'Tony', 'Audrey']
print('Ella' in friends)
