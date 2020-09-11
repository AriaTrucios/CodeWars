"""
 You will have a list of rationals in the form
 { {numer_1, denom_1} , ... {numer_n, denom_n} } 
or
 [ [numer_1, denom_1] , ... [numer_n, denom_n] ] 
or
 [ (numer_1, denom_1) , ... (numer_n, denom_n) ] 
where all numbers are positive ints.
You have to produce a result in the form
 (N_1, D) ... (N_n, D) 
or
 [ [N_1, D] ... [N_n, D] ] 
or
 [ (N_1', D) , ... (N_n, D) ] 
or
{{N_1, D} ... {N_n, D}} 
or
"(N_1, D) ... (N_n, D)"
depending on the language (See Example tests) in which D is as small as possible and N_1/D == numer_1/denom_1 ... N_n/D == numer_n,/denom_n.

Example:

convertFracs [(1, 2), (1, 3), (1, 4)] `shouldBe` [(6, 12), (4, 12), (3, 12)]

Note:
Due to the fact that first translations were written long ago - more than 4 years - these translations have only irreducible fractions. 
Newer translations have some reducible fractions. To be on the safe side it is better to do a bit more work by simplifying fractions even 
if they don't have to be.
"""
import math
def lcm(denoms): # find least common multiple of Denominators list, imported as independant arguments
    least_common_mult = denoms[0]
    for i in denoms[1:]:
        least_common_mult = least_common_mult * i // math.gcd(least_common_mult, i)    # repeatedly goes through each I in Denoms, with LCM = Denoms[0], to finally find Least_Common_Mult of Denoms
    return least_common_mult

def convertFracts(list):
    if len(list) == 0:
        return []
    denoms, nums, ans = [], [], []
    for i in list:
        denoms.append(i[1])
        nums.append(i[0])
    least_common_mult = lcm(denoms)
    for i in range(len(denoms)):
        factor = least_common_mult // denoms[i]
        ans.append( [ int(factor * nums[i]) , least_common_mult ] )
    print(ans)
    
    


convertFracts( [[1, 2], [1, 3], [1, 4]] ) ## [[6, 12], [4, 12], [3, 12]]

"""def gcf(denoms, ):    # returns greatest common factor in given vars

def lcm(*denoms): # find least common multiple of Denominators list, imported as independant arguments
    print(functools.reduce(lambda x, y: math.gcd(x,y), denoms))
    greatest_common_denom = functools.reduce(lambda x, y: math.gcd(x,y), denoms)
    product = functools.reduce(lambda x, y: x * y , denoms)
    print(greatest_common_denom, product)
"""
"""
def gcd(*denoms):    # returns greatest common denom from given list of denominators
    greatest_common_denom = 1
    for i in range(len(denoms) - 1):
        greatest_common_denom = math.gcd(denoms[i], greatest_common_denom)
    print("GCD", greatest_common_denom)
    return greatest_common_denom
"""    
"""    greatest_common_denom = 1
    for n in range(len(denoms)):
        denoms[n] = int(denoms[n])
    for i in denoms:
        greatest_common_denom = math.gcd(greatest_common_denom, i)
        print(greatest_common_denom)
    print(greatest_common_denom)
    return greatest_common_denom
"""
"""
def lcf(denoms): # find least common multiple of Denominators list, imported as independant arguments
    product, gcd, flag = 1, 1, 0
    for i in denoms:
        print("begin loop", i)
        product = product * i   # incriment until product = product of all denoms 
        if flag == 0:            # if first loop, set Prev = I
            flag = 1
            print(gcd, "first pass complete")
            continue
        else:                   # if not first loop
            while i:            # find greatest common denom
                gcd, i = i, gcd % i     # will repeat until i == 0, at which point gcd = greatest common divisor of previous entries. On final loop, gcd = gcd of Denoms
            print(gcd)
    return product / gcd
"""