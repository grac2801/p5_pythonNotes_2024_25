'''
2024-12-09
ogracias
title = intro to dictionaries
'''

# imports


# global variables | constants


# functions


if __name__ == '__main__':
    print('\n\n*******************')
    print('1. Declare a dictionary | Remove last item')
    print('*******************')
    capitals = {'UK': 'London', 'France': 'Paris', 'Germany': 'Berlin'}
    print(capitals)
    # remove last item
    last_item = capitals.popitem()
    print(last_item)
    print(capitals)
    
    print('\n\n*******************')
    print('2. Copy key into a variable, and print')
    print('*******************')
    returned_capital = capitals['UK']
    print(returned_capital)
    
    
    print('\n\n*******************')
    print('3. Adding items to the dictionary')
    print('*******************')
    print(capitals)
    capitals['USA'] = 'Washington DC'
    print(capitals)
    
    
    print('\n\n*******************')
    print('4. copy keys')
    print('*******************')
    capitals = {'UK': 'London', 'France': 'Paris', 'Germany': 'Berlin'}
    returned_countries = capitals.keys()
    print(returned_countries)
    
    
    print('\n\n*******************')
    print('5. Make a dictionary into a list')
    print('*******************')
    print(capitals)
    returned_countries = list(capitals.keys())
    print(returned_countries)
    
    print('\n\n*******************')
    print('6. values()')
    print('*******************')
    returned_values = capitals.values()
    print(returned_values)
    
    #iterate through a dictionary
    for i in capitals.values():
        print(i)
    
    
    print('\n\n*******************')
    print('7. make values into a list')
    print('*******************')
    print(capitals)
    returned_capitals = list(capitals.values())
    print(returned_capitals)
    
    
    
    print('\n\n*******************')
    print('8. popitem() raises keyerror')
    print('*******************')
    capitals = {'Mexico': 'Mexico city'}
    print(capitals)
    returned_item = capitals.popitem()
    print(capitals)
    # returned_item = capitals.popitem()
    # print(capitals)
    
    print('\n\n*******************')
    print('9. Try | Error clause')
    print('*******************')
    capitals = {'UK': 'London', 'France': 'Paris', 'Germany': 'Berlin'}
    try:
        print(capitals['UK'])
        print(capitals['Spain'])
        print(capitals['France'])
    except KeyError:
        print('Country not found')
    
    print('\n\n*******************')
    print('10. get()')
    print('*******************')
    print(capitals)
    print(capitals.get('UK', 'country not found!'))
    print(capitals.get('France', 'country not found!'))
    print(capitals.get('Spain', 'country not found!'))
    
    
    print('\n\n*******************')
    print('11. items()')
    print('*******************')
    print(capitals)
    print(capitals.items())
    
    
    print('\n\n*******************')
    print('12. update a dictionary')
    print('*******************')
    capitals = {'UK': 'London', 'France': 'Paris', 'Germany': 'Berlin'}
    more_capitals = {'Italy': 'Rome', 'Philippines': 'Manila'}
    
    capitals.update(more_capitals)
    print(capitals)
    
    
    
    print('\n\n*******************')
    print('13. copying a dictionary')
    print('*******************')
    car = {
        'brand': 'Ford',
        'model': 'Mustang',
        'year' : 1964
        }
    
    copied_car = car.copy()
    print(car)
    print(copied_car)
    
    print('\n\n*******************')
    print('14. populate a dictionary')
    print('*******************')
    good_students = {
        'Jason' : 100,
        'Mary'  : 98,
        'Luisa' : 100
        }
    
    print(good_students)
    
    # bad students
    students = ['Max', 'John', 'Juan']
    bad_grade = 0
    bad_students = dict.fromkeys(students, bad_grade)
    print(bad_students)
    
    print('\n\n*******************')
    print('15. pop()')
    print('*******************')
    car = {
        'brand': 'Ford',
        'model': 'Mustang',
        'year' : 1964
        }
    print(car)
    car.pop("model")
    print(car)
    
    
    print('\n\n*******************')
    print('16. setdefault()')
    print('*******************')
    car = {
        'brand': 'Ford',
        'model': 'Mustang',
        'year' : 1964
        }
    print(car.setdefault('tire model', '4XMLZC'))
    print(car)
    
    print('\n\n*******************')
    print('17. make a list into a dictionary')
    print('*******************')
    fruits = ['apples', 'pears', 'peaches', 'bananas']
    fruit_dict = dict.fromkeys(fruits, 'in stock')
    print(fruit_dict)
    
    
    print('\n\n*******************')
    print('zip()')
    print('*******************')
    pants = ['jeans', 'shorts', 'shirts']
    prices = [45.50, 24.75, 30.25]
    pants_dict = dict(zip(pants, prices))
    print(pants_dict)
    pants_dict = list(zip(pants, prices))
    print(pants_dict)
    
    
    