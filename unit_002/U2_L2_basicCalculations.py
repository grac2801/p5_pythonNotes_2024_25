'''
2024-09-16
ogracias
title = basic math calculations
'''
x = 37
y = 14
print(f'The answer is ' + str(x + y))
print(f'The answer is {x + y}')

print('\n\n*******************')
print('Let"s convert from F to C')
print('*******************')
f = float(input('Enter the temperature in Fahrenheit degrees: '))
c = (f - 32) * (5/9)
print(f'{f:,.2f} degree(s) is/are equal to {c:,.2f} degree(s)')

#===================================================================================================
# Student activity:
# complete the Celsius to Fahrenheit equation and solve it.
#===================================================================================================
c = float(input('Enter your temperature in Celsius degrees: '))
f = (c * (9/5) + 32)
print(f'The Fahrenheit equivalent to {c:.2f} degrees is {f:.2f} degrees')

print('*******************')
print('exponents')
print('*******************')
print('4 to the power of 3:', 4**3)

#===============================================================================
# Student activity
#
# a) You will ask a user to state how many recyclable container they have that
# are below and above 1L. The container below 1L will get $0.10 and above will
# get $0.25. Your program will read the input, and display the refund. Output
# the correct amount of money the customer will get displaying $ and cents to
# the correct number of decimals.
#===============================================================================
print('\n********************')
print('recyclable')
print('********************')
below1L = float(input('How many containers below 1L do you have? '))
above1L = float(input('How many containers above 1L do you have? '))

subtotalBelow = below1L * .1
subtotalAbove = above1L * .25


refund = subtotalAbove + subtotalBelow
print('\n********************')
print('---Receipt---')
print('********************')
print(f'Above 1L \u2192 ${subtotalAbove:<,.2f}')
print(f'Below 1L \u2192 ${subtotalBelow:<,.2f}')
print(f'Total refund \u2192 ${refund:<,.2f}')
    

