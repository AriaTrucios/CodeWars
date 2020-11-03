"""
Create a function that differentiates a polynomial for a given value of x.

Your function will receive 2 arguments: a polynomial as a string, and a point to evaluate the equation as an integer.
Assumptions:

    There will be a coefficient near each x, unless the coefficient equals 1 or -1.
    There will be an exponent near each x, unless the exponent equals 0 or 1.
    All exponents will be greater or equal to zero

Examples:

differenatiate("12x+2", 3)      ==>   returns 12
differenatiate("x^2+3x+2", 3)   ==>   returns 9
"""
def differentiate(equation, point):
    # List is going to be what you throw each component into
    # Counter is how you're going to keep track of position in List
    list, counter = [""], 0
    for l in equation:
        # catches + or - symbols, ONLY if not first str (so you don't miss negative integers) 
        # increase counter by 2 because you chucked the symbol into a spot and append empty spot "" for first if statement
        if (l == "+" or l == "-") and list[counter] != "":
            list.append(l)
            list.append("")
            counter += 2
            continue
        # catches all other letters and puts them at end of string in current position list[counter]
        # NOTE: don't have to worry about negative exponents per rules
        else:
            list[counter] = f"{list[counter]}" + l
            continue
    for n in range(0,counter + 1):
        if list[n] == "+" or list[n] == "-":
            continue
        elif "x" not in list[n]:
            list[n] = "0"
            continue
        elif "^" in list[n]:
            coefficient, exponent = list[n].split("^")
            # if only "x", treat it like a 1, otherwise cut everything off except x
            if coefficient == "x":
                coefficient = 1
            elif coefficient == "-x":
                coefficient = -1
            else:
                coefficient = coefficient[:-1]
            list[n] = int(coefficient) * int(exponent) * (point**(int(exponent) - 1))
            continue
        else:
            # case of not having an exponent
            if list[n] == "x":
                list[n] = 1
            elif list[n] == "-x":
                list[n] = -1
            else:
                list[n] = int(list[n][:-1])
            continue
    # M becomes every odd integer up to but NOT including Counter. M points at position of "+" or "-" in List
    solution = int(list[0])
    for m in range(1,counter,2):
        if list[m] == "+":
            solution += int(list[m+1])
        # for the subtraction case
        else:
            solution -= int(list[m+1])
    return solution

differentiate("x^2+12x-3", 3) # 2x+12 | should return 18

"""
from collections import defaultdict
import re

P = re.compile(r'\+?(-?\d*)(x\^?)?(\d*)')

def differentiate(eq, x):
    
    derivate = defaultdict(int)
    for coef,var,exp in P.findall(eq):
        exp  = int(exp or var and '1' or '0')
        coef = int(coef!='-' and coef or coef and '-1' or '1')
        
        if exp: derivate[exp-1] += exp * coef
    
    return sum(coef * x**exp for exp,coef in derivate.items())

__________________________________________
def parse_monom(monom):
    if 'x' not in monom: monom = monom + 'x^0'
    if monom.startswith('x'): monom = '1' + monom
    if monom.startswith('-x'): monom = '-1' + monom[1:]
    if monom.endswith('x'): monom = monom + '^1'
    coefficient, degree = map(int, monom.replace('x', '').split('^'))
    return degree, coefficient

def differentiate(equation, point):
    monoms = equation.replace('-', '+-').lstrip('+').split('+')
    polynom = dict(map(parse_monom, monoms))
    return sum(coefficient * degree * point ** (degree - 1)
               for degree, coefficient in polynom.items() if degree)
               
"""