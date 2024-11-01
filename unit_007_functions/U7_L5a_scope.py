'''
2024-10-30
ogracias
topic = scope
'''
x = 5

# imports



# functions
def change_x(parameter):
    global x
    global y
    x *= parameter
    print('from inside function', x)
    


if __name__ == '__main__':
    print('original x =', x)
    print('\n\nFunction call')
    change_x(100)
    
    print('\n\nAfter function =', x)
    
    
    