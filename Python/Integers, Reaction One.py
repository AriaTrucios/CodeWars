"""
Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors squared are: 1, 4, 9, 36, 49, 196, 441, 1764. 
The sum of the squared divisors is 2500 which is 50 * 50, a square!

Given two integers m, n (1 <= m <= n) we want to find all integers between m and n whose sum of squared divisors is itself a square. 42 is such a number.

The result will be an array of arrays or of tuples or a string, each subarray having two elements,
first the number whose squared divisors is a square and then the sum of the squared divisors.
#Examples:

list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
list_squared(42, 250) --> [[42, 2500], [246, 84100]]
"""
import math
def list_squared(m, n):
    the_ultimate_list = [] #collect the values we want
    for number in range(m, n+1): # incriments Number for all values from m to n
        current_sum = 0
        for i in range(1, int(math.sqrt(number)) + 1): # incriments I from 1 to Number/2 - will have to add case to add Number to list
            if number % i == 0 and not i == number:
                current_sum = current_sum + (i ** 2)
                if number // i != i:
                    current_sum = current_sum + (number // i) ** 2
                pass
            if i == number:
                current_sum = current_sum + (number ** 2) # if I == Number, then we must add its square to sequence and continue
                pass
            if i == int(math.sqrt(number)): # if I is last number in sequence - which will not be a divisor, check if Current_Sum is a square
                x = math.sqrt(current_sum)   # creates X, which is the greatest floor of exact sqrt of Current_Sum
                if ( x - math.floor(x) == 0):      # if X - floor(x) == 0, then Current_Sum is a perfect square
                    the_ultimate_list.append( [ number, current_sum ] )
                    continue
                else:       # the case where Current_Sum is not a perfect square
                    continue
            else:           # for I that is not a divisor of Number
                continue
    print(the_ultimate_list)
    return the_ultimate_list