'''
Created on Feb 21, 2025

@author: ogracias
'''

if __name__ == '__main__':
    print('\n\n*******************')
    print('comprehensions with numbers')
    print('*******************')
    nums = [1, 2, 3, 4, 5]
    print(nums)
    
    results = []
    def timesTwo(aList):
        for i in nums:
            i = i * 2
            results.append(i)
        return results
    
    
    nums2 = timesTwo(nums)
    print(nums2)
    
    nums3 = [ i * 4 for i in nums]
    print(nums3)
    
    print('\n\n*******************')
    print('comprehensions using text')
    print('*******************')
    
    strings = ['welcome', 'to', 'computer', 'science']
    print(strings)
    #let's capitalize each word using comprehensions
    results2 = [i.upper() for i in strings]
    print(results2)
    
    print('\n\n*******************')
    print('functions and comprehensions')
    print('*******************')
    def timesFive(num):
        return num * 5
    
    new_nums = [timesFive(i) for i in nums]
    print(new_nums)
    
    def timesTen(num):
        num = num * 10
        return num
    
    answer_function = [timesTen(n) for n in nums if n > 2]
    print(answer_function)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    