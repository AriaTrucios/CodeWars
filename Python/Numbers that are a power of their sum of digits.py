"""The number 81 has a special property, a certain power of the sum of its digits is equal to 81 (nine squared).
Eighty one (81), is the first number in having this property (not considering numbers of one digit). 
The next one, is 512. Let's see both cases with the details

8 + 1 = 9 and 92 = 81

512 = 5 + 1 + 2 = 8 and 83 = 512

We need to make a function, power_sumDigTerm(), that receives a number n and may output the n-th term of this sequence of numbers. 
The cases we presented above means that
power_sumDigTerm(1) == 81
power_sumDigTerm(2) == 512
"""
from math import log
def check_ifPowSum(n):
    total = sum(map(int,str(n))) # Total = sum of digits in n
    try:
        if total ** int(round(log(n, total))) == n and int(round(log(n, total))) > 1: # checks to see if Total ** (some power calculated by log base total of n) == n, then PowSum = True
            print(n, total, int(round(log(n, total))))
    except:
        print('No')

def next_sumdig(n=2):
    for i in range(n, 100000000):
        total = sum(map(int,str(i))) # Total = sum of digits in n
        try:
            power = int(round(log(i, total))) # Power = the power needed for I ** Power == N
            if total ** power == i and power > 1: 
                    # checks to see if Total ** Power == n AND that power IS GREATER THAN 1, then PowSum = True
                print(i, total, power)
        except:
            pass
    print(i)


next_sumdig()

"""
from math import log
def check_ifPowSum(n):
    total = sum(map(int,str(n))) # Total = sum of digits in n
    power = int(round(log(n, total)))
    if total ** power == n and power > 1: # checks to see if Total ** (some power calculated by log base total of n) == n, then PowSum = True
        print(n, total, power)
"""