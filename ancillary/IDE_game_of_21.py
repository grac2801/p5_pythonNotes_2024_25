from random import shuffle
from random import randint
import re
  
  
def play(P, shuffled):
    total = 0
    print(P, ':')
    for i in range(3):
        card = shuffled
        print(card)
        if nums.isdigit():
            total += int(nums)
        elif nums == "J" or nums == "Q" or nums == "K":
            total += 10
        elif nums == 'ace':
            ace = int(input('ace (1 or 11): '))
            total += ace
        else:
            total += 0
            print('Total: ', total)
    return total
        
  
if __name__ == '__main__':
    txt = "hello, my name is Peter, I am 26 years old"
    total = 0
    y = []
    x = re.split("[,. ]", txt)
    for i in range(len(x)):
        if x[i] == '':
            continue
        elif x[i].isdigit():
            total += (int)(x[i])
        else:
            y.append(x[i])
        
    print(x)
    print(y)
    print(total)
    p1 = input('P1(name):')
    p2 = input('P2(name):')
    card = ['hearts', 'diamonds', "clubs", 'spades']
    nums = ["2", "3", "4", '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'ace']
    deck = []
    for c in card:
        for n in nums:
            deck.append(n +" of "+ c)
    # make a for loop which iterates and populates the deck list
    
    chosen = randint(0, 51)
    
    shuffled = deck[chosen]
    print(shuffled)
    
    first = shuffled.index(" ", 0, 5)
    print(first)    
    
    
    # T1 = play(p1, shuffled)
    # T2 = play(p2, shuffled)
    # print(p1, ":", T1 ,',', p2 ,':', T2)
    # if T1 == T2:
    #     print("Tie")
    # elif T1 < T2:
    #     print("Player 1 wins")
    # else:
    #     print("Player 2 wins")