'''
2025-02-10
ogracias
title = intro to 2D lists
'''

# imports


# global variables | constants


# functions


if __name__ == '__main__':
    newGrades = [[9, 8, 7, 8],
                 [8,10, 6, 8],
                 [5, 9, 7, 9]
                ]
    
    #YOU USE THIS METHOD WHEN CHECKING OR PRINTING. YOU CAN NOT CHANGE THE 2D LIST
    for row in newGrades:
        for col in row:
            print(f"{col:^3}{'|':1}", end='')
        print()
    
    #===============================================================================================
    # Let's find out how many A's students got. (9 or 10 = A)
    #===============================================================================================
    count = 0
    for row in newGrades:
        for col in row:
            if col >= 9:
                count += 1
    print(f"The class got {count} A grades in the exam\n\n")
    
    
    #YOU USE THIS METHOD WHEN CHANGING ANYTHING ON THE 2D LIST
    #===============================================================================================
    # change all 8s to 2s
    #===============================================================================================
    for row in range(len(newGrades)):
        for col in range(len(newGrades[row])):
            if(newGrades[row][col] == 8):
                newGrades[row][col] = 2
                
    #to print
    for row in range(len(newGrades)):
        for col in range(len(newGrades[row])):
            print(f"{newGrades[row][col]:^4}", end='')
        print()
    
    
    #===============================================================================================
    # appending arrays to your 2D array
    #===============================================================================================
    grades = []
    grades.append([85, 76, 82])
    grades.append([90, 79, 88])
    grades.append([100, 98, 91])
    print(grades)
    
    grades[1][0] = 100
    print(grades)
    
    moreGrades = [60, 70, 80]
    grades[2].extend(moreGrades)
    print(grades)
    
    #===============================================================================================
    # STUDENT ACTIVITY -> Add a point to every grade in newGrades and then print it.
    #===============================================================================================
    newGrades = [[9, 8, 7, 8],
                 [8, 7, 6, 8],
                 [5, 9, 7, 9]
                ]
    for row in range(len(newGrades)):
        for col in range(len(newGrades[row])):
            newGrades[row][col] += 1
    #no indices
    print("print it")
    for r in newGrades:
        for c in r:
            print(f"{c:^4}{'|'}", end='')
        print()
    
    
    
    
    
    
    
    