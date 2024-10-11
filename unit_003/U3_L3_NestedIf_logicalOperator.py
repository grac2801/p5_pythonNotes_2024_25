'''
2024-10-11
ogracias
topic = nested if | logical operators
'''

# imports
print('\n\n********************')
print('nested ifs answer 1')
print('********************')
n = int(input('Enter a number: '))
if n >= 0:
    if(n <= 100):
        print('Grade is valid.')
        print('No errors')
print('Done!!')


print('\n\n********************')
print('nested ifs answer 2')
print('********************')
#===============================================================================
# 3 logical operators= and, or, not
#===============================================================================
n = int(input('Enter another number: '))
if (n >= 0 and n <= 100):
    print('Grade is valid')
    print('No errors')
print('Done!!')


#===============================================================================
# Activity:
# code a grading system from
# 90 - 100 A
# 80 - <90 B
# less than 60 is an F
# any grade lower than 0 or greater than 100 --> Error
# Use  of and | or
#===============================================================================
grade = float(input('Enter the grade: '))
if grade >= 90 and grade  <= 100:
    print('A')
if grade >= 80 and grade  < 90:
    print('B')
if grade >= 70 and grade  < 80:
    print('C')
if grade >= 60 and grade  < 70:
    print('D')
if grade < 60 and grade >= 0:
    print('F')
if grade < 0 or grade > 100:
    print('Error')


print('\n\n********************')
print('not')
print('********************')
another_grade = int(input('Enter another grade: '))
if not(grade >= 80):
    print('Failed')























