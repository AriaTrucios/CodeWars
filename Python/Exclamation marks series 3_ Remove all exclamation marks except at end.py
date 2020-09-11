"""Description:

Remove all exclamation marks from sentence except at the end.
Examples

remove("Hi!") == "Hi!"
remove("Hi!!!") == "Hi!!!"
remove("!Hi") == "Hi"
remove("!Hi!") == "Hi!"
remove("Hi! Hi!") == "Hi Hi!"
remove("Hi") == "Hi"
"""
def remove(s):
    #s.find('!') # returns position in string.
    done = 0
    reverse = s[::-1]
    for char in reverse:
        print(s.find(char))
        if char == '!' and done == 0:
            continue
        elif char == '!' and done != 0:
            
            continue
        else:
            done = 1
            continue
remove("!HELL!O!!")
            
"""def remove(s):
    #s.find('!') # returns position in string.
    done = 0
    reverse = s[::-1]
    for char in reverse:
        print(s.find(char))
        if char == '!' and done == 0:
            continue
        elif char == '!' and done != 0:
            
            continue
        else:
            done = 1
            continue"""