'''
2024-10-11
ogracias
topic = elif
'''

# imports

pH_table = '''
pH level          Category
0 - 4             Strong acid
5 - 6              Weak acid
7                  Neutral 
8 - 9              weak base
10 - 14            Strong base
'''
print(pH_table)


value = float(input('Enter the pH level displayed: '))
if value > 0:
    if value < 7:
        print('It is acidic, be careful')
    elif value > 7 and value <= 14:
        print('It is basic')
    elif value == 7:
        print('Pure water')
elif value < -10:
    print('your value is < -10')
else:
    print('Your value is the else statement')








