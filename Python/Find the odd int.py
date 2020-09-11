"""Given an array, find the integer that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""
def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 == 1:
            print(i)
            return i
        else: continue


find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])