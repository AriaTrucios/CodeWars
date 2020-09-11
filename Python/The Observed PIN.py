"""
https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python

Alright, detective, one of our colleagues successfully observed our target person, Robby the robber. We followed him to a secret warehouse, where we assume 
to find all the stolen stuff. The door to this warehouse is secured by an electronic combination lock. 
Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.

The keypad has the following layout:
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another adjacent digit 
(horizontally or vertically, but not diagonally). E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8.
He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, they never finally lock the system or sound the alarm. 
That's why we can try out all possible (*) variations.

* possible in sense of: the observed PIN itself and all variations considering the adjacent digits

Can you help us to find all those variations? It would be nice to have a function, that returns an array (or a list in Java and C#) of all variations 
for an observed PIN with a length of 1 to 8 digits. We could name the function getPINs (get_pins in python, GetPINs in C#). But please note that all PINs, 
the observed one and also the results, must be strings, because of potentially leading '0's."""

from itertools import product
def get_pins(obs):
    total_possabilities, every_combination = [], []
    for i in obs:
        current_possabilities = []
        if i == '0':
            current_possabilities.append('8')
            current_possabilities.append('0')
            total_possabilities.append(current_possabilities)
            continue
        if i == '8':
            current_possabilities.append('0')
        if int(i) % 3 == 0: #if I is in right row
            current_possabilities.append(str(int(i)-1))
            current_possabilities.append(str(int(i)))
        if int(i) % 3 == 1:
            current_possabilities.append(str(int(i)))
            current_possabilities.append(str(int(i)+1))
        if int(i) % 3 == 2:
            current_possabilities.append(str(int(i)-1))
            current_possabilities.append(str(int(i)))
            current_possabilities.append(str(int(i)+1))
        if 0 < int(i) / 3 <= 1:
            current_possabilities.append(str(int(i)+3))
        if 1 < int(i) / 3 <= 2:
            current_possabilities.append(str(int(i)+3))
            current_possabilities.append(str(int(i)-3))
        if int(i) / 3 > 2:
            current_possabilities.append(str(int(i)-3))
        total_possabilities.append(current_possabilities)
        print(i, current_possabilities)
    every_combination = list(set([''.join(x) for x in product(*total_possabilities)]))
    return(every_combination)

print(get_pins('12345'))

##################
# SIMPLEST SOLUTION
##################

from itertools import product

ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')

def get_pins(observed):
    return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]

print(get_pins('123'))