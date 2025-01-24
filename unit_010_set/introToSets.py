'''
2025-01-24
ogracias
title = intro to sets
'''

# imports


# global variables | constants


# functions


if __name__ == '__main__':
    print('\n\n*******************')
    print('create a set')
    print('*******************')
    empty_set = set()
    print(empty_set)
    
    even_numbers = {2, 4, 6, 8}
    print(even_numbers)
    
    letters = set('letters')
    print(letters)
    # No duplicates, no index, dictionary with no values, order is irrelevant
    
    
    print('\n\n*******************')
    print('Make a set from a list')
    print('*******************')
    reindeers_list = ['Dasher', 'Prancer', 'Dancer', 'Dancer']
    reindeers_set = set(reindeers_list)
    print(reindeers_set, 'length of set:', len(reindeers_set))
    
    print('\n\n*******************')
    print('Make a tuple into a set')
    print('*******************')
    sea_animals_tuple = ('dolphin', 'whale', 'fish', 'dolphin')
    sea_animals_set = set(sea_animals_tuple)
    print(sea_animals_set)
    
    
    print('\n\n*******************')
    print('when given a dictionary, set only uses keys')
    print('*******************')
    fruits_dict = {
                'apple': 'red',
                'orange': 'orange',
                'pear' : 'green',
                'banana': 'yellow'
                    }
    fruits_set = set(fruits_dict)
    print(fruits_set)
    
    #===============================================================================================
    # SET methods
    #===============================================================================================
    animals = {
            'bipedal' : {'humans', 'kangaroo'},
            'carnivore': {'lion', 'pig'},
            'omnivore' : {'humans', 'pig', 'chimpanzee'},
            'hervibore': {'pig', 'cow', 'deer', 'humans'},
            'quadripedal': {'dog', 'lion'},
            'smart' : {'humans', 'whales', 'chimpanzee'}
                }
    print('animals', animals)             
    
    # list which types have humans in them
    counter = 0
    for k, v in animals.items():
        if 'humans' in v:
            counter += 1
            print(counter, '-', k)
    
    
    #===============================================================================================
    # which types have humans and either chimpanzee or kangaroo
    #===============================================================================================
    for types, creatures in animals.items():
        if 'humans' in creatures and ('kangaroo' in creatures or 'chimpanzee' in creatures):
            print(types)
    
    print('\n\n')
    #===============================================================================================
    # which types have humans but not kangaroos
    #===============================================================================================
    for types, creatures in animals.items():
        if ('humans' in creatures and ('kangaroo' not in creatures)):
            print(types)
        
        
    print('\n\n*******************')
    print('& or intersection')
    print('*******************')
    #print both humans and chimpanzees
    for types, creatures in animals.items():
        if creatures & {'chimpanzee'} and creatures & {'humans'}:
            print(types)
    
    #print humans or chimpanzees
    for types, creatures in animals.items():
        if creatures.intersection('chimpanzee') or creatures.intersection('humans'):
            print(types)
        
    
    #===============================================================================================
    # which animals have humans, but neither chimpanzee nor pig
    #===============================================================================================
    for types, creatures in animals.items():
        if 'humans' in creatures and not creatures & {'chimpanzee', 'pig'}:
            print(types)
        
    
    set_a = {1, 2}
    set_b = {2, 3}
    print(set_a & set_b)
    print(set_a.intersection(set_b))
    
    
    print('\n\n*******************')
    print('union or |')
    print('*******************')
    set_a = {1, 2}
    set_b = {2, 3}
    print(set_a.union(set_b))
    print(set_a | set_b)
    
    
    print('\n\n*******************')
    print('difference or -')
    print('*******************')
    set_a = {1, 2}
    set_b = {2, 3}
    print(set_a - set_b)
    print(set_a.difference(set_b))
    
    
    print('\n\n*******************')
    print('symmetric_difference or ^')
    print('*******************')
    #items in one set or the other, but not both
    set_a = {1, 2}
    set_b = {2, 3}
    print(set_a ^ set_b)
    print(set_a.symmetric_difference(set_b))
    
    
    print('\n\n*******************')
    print('issubset() or <=')
    print('*******************')
    set_a = {1, 2}
    set_b = {1, 2, 3}
    print(set_a <= set_b)
    
    print('\n\n*******************')
    print('issuperset() or >=')
    print('*******************')
    set_a = {1, 2}
    set_b = {1, 2, 3}
    print(set_b.issuperset(set_a))
    print(set_a.issuperset(set_b))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        