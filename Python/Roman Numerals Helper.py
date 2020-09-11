"""
Task

Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.
Examples

RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000

Help

| Symbol | Value | |----------------| | I | 1 | | V | 5 | | X | 10 | | L | 50 | | C | 100 | | D | 500 | | M | 1000 |
"""
"""
class RomanNumerals:
    def to_roman( int ):
        pass
    def from_roman( str ):
        pass

IV = 4
IX
IIX

*go down list right to left
if it's in ascending value from right to left, continue
if you step down in value, then ISOLATE THAT CHUNK, strip it out, add it to the sum chunk

for constructing roman numerals, if the value is above 6, then combine things like usual
if its above 6, use subtraction model
"""
class RomanNumerals:
    def to_roman(int):
        ROMAN_INTS = [
        [100, 'M', 'D', 'C'],
        [10, 'C', 'L', 'X'],
        [1, 'X', 'V', 'I']]
        working_string = ''
        if int // 1000 != 0:
            working_string = working_string + 'M' * (int // 1000)
            int = int % 1000
        for i in range(3):
            if int // ROMAN_INTS[i][0] == 9:
                working_string = working_string + ROMAN_INTS[i][3] + ROMAN_INTS[i][1]
                int = int - ROMAN_INTS[i][0] * 9
            elif int // ROMAN_INTS[i][0] >= 5: # case where current I is a multiple of 5, so don't consider IV or CM tomfoolery
                working_string = working_string + ROMAN_INTS[i][2]
                int = int % (ROMAN_INTS[i][0] * 5)
            elif int // ROMAN_INTS[i][0] == 4:
                working_string = working_string + ROMAN_INTS[i][3] + ROMAN_INTS[i][2]
                int = int - ROMAN_INTS[i][0] * 4
            working_string = working_string + ROMAN_INTS[i][3] * (int // ROMAN_INTS[i][0] )
        return working_string

    def from_roman(str):
        ROMAN_VAL = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        working_sum = 0
        for i in range(len(str)):
            if i > 0 and ROMAN_VAL[str[i]] > ROMAN_VAL[str[i-1]]:
                working_sum += ROMAN_VAL[str[i]] - 2 * ROMAN_VAL[str[i-1]]
            else:
                working_sum += ROMAN_VAL[str[i]]
        return(working_sum)
    

print(RomanNumerals.from_roman('MMCMCLXXIX'))
print(RomanNumerals.to_roman(2008))

###########################
# BEST ANSWER
###########################

"""
import string
from collections import OrderedDict

class RomanNumerals:
  @classmethod
  def to_roman(self, num):
    conversions = OrderedDict([('M',1000), ('CM',900), ('D', 500), ('CD',400), ('C',100), ('XC',90), ('L',50), ('XL',40),
                               ('X',10), ('IX',9), ('V',5), ('IV',4), ('I',1)])
    out = ''
    for key, value in conversions.iteritems():
      while num >= value:
        out += key
        num -= value
    return out
  
  @classmethod
  def from_roman(self, roman):
    conversions = OrderedDict([('CM',900), ('CD',400), ('XC',90), ('XL',40), ('IX',9), ('IV',4), ('M',1000), ('D',500),
                               ('C',100), ('L',50), ('X',10), ('V',5), ('I',1)])
    out = 0
    for key, value in conversions.iteritems():
      out += value * roman.count(key)
      roman = string.replace(roman, key, "")
    return out
"""