'''
2024-12-04
ogracias
title = Lists as parameters
'''

# imports


# global variables | constants


# functions
def change(a):
    a += 1

def changeArray(a):
    for i in range(len(a)):
        a[i] += 1
        
        
        
def changePositions(position1, position2, colorsArray):
    temp = colorsArray[position1 - 1]
    colorsArray[position1 - 1] = colorsArray[position2 - 1]
    colorsArray[position2 - 1] = temp
    

if __name__ == '__main__':
    # passing by value [example with simple numbers]
    x = 5
    print(x)
    change(x)
    print(x)
    
    # Passing objects | passing by reference
    x = [2, 5, 6, 8]
    print(x)
    changeArray(x)
    print(x)
    
    # swapping values
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    choice1 = int(input('Enter the first element you want to swap: '))
    choice2 = int(input('Enter the second element you want to swap: '))
    changePositions(choice1, choice2, colors)
    print(colors)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
