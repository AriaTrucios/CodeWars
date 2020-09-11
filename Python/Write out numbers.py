"""
Create a function that transforms any positive number to a string representing the number in words.
The function should work for all numbers between 0 and 999999.
Examples
number2words(0)  ==>  "zero"
number2words(1)  ==>  "one"
number2words(9)  ==>  "nine"
number2words(10)  ==>  "ten"
number2words(17)  ==>  "seventeen"
number2words(20)  ==>  "twenty"
number2words(21)  ==>  "twenty-one"
number2words(45)  ==>  "forty-five"
number2words(80)  ==>  "eighty"
number2words(99)  ==>  "ninety-nine"
number2words(100)  ==>  "one hundred"
number2words(301)  ==>  "three hundred one"
number2words(799)  ==>  "seven hundred ninety-nine"
number2words(800)  ==>  "eight hundred"
number2words(950)  ==>  "nine hundred fifty"
number2words(1000)  ==>  "one thousand"
number2words(1002)  ==>  "one thousand two"
number2words(3051)  ==>  "three thousand fifty-one"
number2words(7200)  ==>  "seven thousand two hundred"
number2words(7219)  ==>  "seven thousand two hundred nineteen"
number2words(8330)  ==>  "eight thousand three hundred thirty"
"ninety-nine thousand nine hundred ninety-nine"
"eight hundred eighty-eight thousand eight hundred eighty-eight
"""
def number2words(n):
    input = str(n) # converts N to string for manipulation
    if len( input ) > 3: # if the length of N is > 3
        # pass the characters from position 0 to [ 3 less than len(N) ] (ie 123456 -> 123) into slicer, assign to Thou_Word
        thou_word = f"{slicer( input[ 0 : len(input) - 3 ] )} thousand"
        # pass characters from position [ 3 less than len(N) to rest of word ] into slicer, asssign to Hundreds_and_Lower_Word
        if input[ len(input) - 3 : ] == '000':
            return(f"{thou_word}")
        else:
            hundreds_and_lower_word = slicer( input[ len(input) - 3 : ] )
        return(f"{thou_word} {hundreds_and_lower_word}")
    else:
        return slicer( input )

def slicer( str ):
    if len( str ) == 3:
        reply = hunds( str ) 
    elif len( str ) == 2:
        reply = tens( str )
    elif len( str ) == 1:
        reply = ones( str )
    return( reply )

def hunds( str ):
    if str[ 0 ] == '0':
        return(tens( str[1:] ))
    elif str[ 1 ] == '0' and str[ 2 ] ==  '0':
        return(f"{ones(str)} hundred")
    else:
        return(f"{ones(str)} hundred {tens( str[1:] )}")

def tens( str ):
    if str[0] == '0':
        return(ones( str[1] ))
    elif str[0] == '1': # handle as a teens case
        selection = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
        return( selection [ int( str[1] ) ] ) # Str = 12 --> looks at pos 1 = '2', selects selection[2] = 'twelve'
    else:
        selection = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
        if str[1] == '0': # if ends with 0, just reply with 10s place response
            return(f"{selection[ int( str[0] ) ]}")
        else:             # else, reply with 10s place and kick to 1s place
            return(f"{selection[ int( str[0] ) ]}-{ ones( str[1] ) }")

def ones( str ):
    selection = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    return( selection[ int( str[0] ) ] ) # returns string corresponding to String's position in Selection



## ELEGANT SOLUTION ##

words = "zero one two three four five six seven eight nine" + \
" ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty" + \
" thirty forty fifty sixty seventy eighty ninety"
words = words.split(" ")

def number2words(n):
    if n < 20:
        return words[n]
    elif n < 100:
        return words[18 + n // 10] + ('' if n % 10 == 0 else '-' + words[n % 10])
    elif n < 1000:
        return number2words(n // 100) + " hundred" + (' ' + number2words(n % 100) if n % 100 > 0 else '')
    elif n < 1000000:
        return number2words(n // 1000) + " thousand" + (' ' + number2words(n % 1000) if n % 1000 > 0 else '')