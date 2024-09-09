'''
Created on Sep 9, 2024

@author: ogracias
'''
print("Hello World. It is me again")

# default separator -- sep
print('Hello', 'Mr.', 'Gracias')#implicit separator
print('Hello ' + 'Mr. ' + "Gracias")#concatenation = glue together

#Explicit separator
print('Today', 'is a very hot', 'day', sep=" + ")
print('5'+ '10')
print(5 + 10)

# implicit end of string
print('My name is', 'Mr. Gracias', end=". End\n")
print('How are you?')

firstNumber = 5
secondNumber = 10

print(firstNumber)
print(secondNumber)


print(firstNumber, end=' and ')
print(secondNumber)

#formatting
myAge = 53
favoriteColor = 'dark blue'
print('I am {0} years old, and my favorite color is {1}.'.format(myAge, favoriteColor))
print('I am {1} years old, and my favorite color is {0}.'.format(myAge, favoriteColor))
print('I am {0} years old, and my favorite color is {1}.'.format(myAge, favoriteColor))

#better formatting
print(f'I am {myAge} years old, and my favorite color is {favoriteColor}')











