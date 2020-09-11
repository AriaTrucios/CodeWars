"""In this kata, you must create a digital root function.

A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.

Here's how it works:

digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6

digital_root(132189)
=> 1 + 3 + 2 + 1 + 8 + 9
=> 24 ...
=> 2 + 4
=> 6

digital_root(493193)
=> 4 + 9 + 3 + 1 + 9 + 3
=> 29 ...
=> 2 + 9
=> 11 ...
=> 1 + 1
=> 2"""
def digital_root(n):
    sum = 0
    for i in str(n):
        sum = sum + int(i)
    if len(str(sum)) == 1:
        print(sum)
        return sum
    else:
        return digital_root(sum)


digital_root(16) # 7
digital_root(456) # 6

##optimal solution:

def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))