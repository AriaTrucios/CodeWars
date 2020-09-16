""" Link: https://www.codewars.com/kata/58d06bfbc43d20767e000074/train/python
You will need to create a function that takes two arguments, the playing board and the attacks.

Boats are placed either horizontally, vertically or diagonally on the board. 0 represents a space not occupied by a boat. 
Digits 1-3 represent boats which vary in length 1-4 spaces long. There will always be at least 1 boat up to a maximum of 3 in any one game. 
Boat sizes and board dimentions will vary from game to game.

Attacks are calculated from the bottom left, first the X coordinate then the Y. There will be at least one attack per game, and the array will not contain duplicates.

[[2, 1], [1, 3], [4, 2]]

Scoring
1 point for every whole boat sank.
0.5 points for each boat hit at least once (not including boats that are sunk).
-1 point for each whole boat that was not hit at least once. 

Sunk or Damaged
`sunk` = all boats that are sunk
`damaged` = all boats that have been hit at least once but not sunk
`notTouched/not_touched` = all boats that have not been hit at least once 

Output

You should return a hash with the following data

`sunk`, `damaged`, `not_touched`, `points`
{ 'sunk': 0, 'damaged': 2 , 'not_touched': 1, 'points': 0 }

Function Initialization

board = [[0,0,0,2,2,0],
         [0,3,0,0,0,0],
         [0,3,0,1,0,0],
         [0,3,0,1,0,0]]
attacks = [[2, 1], [1, 3], [4, 2]]
damaged_or_sunk(board, attacks)
"""

def calculate_score(sunk, damaged, not_touched):
    #calculates points from inputs
    points = sunk + (0.5 * damaged) + (-1 * not_touched)

    # returns int of points if points is a whole # (points % 1 == 0 for whole), else return float
    return int(points) if points % 1 == 0 else points 


"""def battle(aftermath_map, hits, attacks): 
    # goes through each attack and builds 2 return arrays
    # aftermath_map = combination of hits and board, hits = hits_map
    for i in attacks:
            # find target location for new attack
        x_pos = len(aftermath_map[0]) - 1 - i[0]
            # len(aftermath_map[0]) - 1 : gives indexed max pos of aftermath_map's "x" position
            # - attacks[0][0] : subtracts x pos of next indexed attack
            # X_pos is now pointing at the horizontal position of the next attack

        y_pos = len(aftermath_map) - 1 - i[1]
            # len(boaaftermath_maprd) - 1 : gives indexed max pos of aftermath_map's "y" position
            # - attacks[0][0] : subtracts y pos of next indexed attack
            # Y_pos is now pointing at the vertical position of the next attack

        # if miss, move on to next attacks item
        if aftermath_map[y_pos][x_pos] == 0:
            continue
        
        else:
            hits[y_pos][x_pos] = "#" # use "#" to indicate hits
            aftermath_map[y_pos][x_pos] = "#"
            continue
    return aftermath_map, hits
    # aftermath_map = combination of hits and board, hits = hits_map"""

def battle(map, attacks): 
    # build hits_map array to track locations where hits have occurred
    # hits_map = [[0 for i in range(len(map[0]))] for j in range(len(map))]   # blank array to track what gets hit
    ship_map = [row[:] for row in map]
    letters_hit = []
    for i in attacks:
        x_pos = len(map[0]) - 1 - i[0]
        y_pos = len(map) - 1 - i[1]
        if map[y_pos][x_pos] == 0:
            continue
        else:
            if map[y_pos][x_pos] not in letters_hit:
                letters_hit.append(map[y_pos][x_pos])
            map[y_pos][x_pos] = "#" # use "#" to indicate hits_map
            continue
    return map, letters_hit, ship_map



def ship_identifier(map):
    #converts map to ship_map, which uses a unique letter for each vessel, starting with "a" == chr(97)
    ship_map = [row[:] for row in map]
    print("check this matches board")
    print(ship_map)
    ship_count = 0                 # ship_count will be flag to keep track of which unique character we're on
    for j in range(len(ship_map)): # J = each position in "y" axis of ship_map
        for i in range(len(ship_map[0])):  # I = each position in "x" axis of ship_map
            print(j,i, ship_map[j][i])
            if ship_map[j][i] == 0 or type(ship_map[j][i]) == str: 
                continue                # if current position is 0 -empty-, or is a string, move on
            elif ship_map[j][i] == 1:
                ship_map[j][i] = chr(ship_count + 97) 
                ship_count += 1    # reassign current position to next unique char, in order
                continue                # with Unique_Identit = 0 giving chr(97) = "a"
            
            # at this point, the current value at ship_map[j][i] is NOT a string, 0, or 1
            # time to go hunting for ships >1 in length
            
            else:
                if i < len(ship_map[0]) - 1 and ship_map[j][i+1] == ship_map[j][i]:    # the ship is horiz!
                    if ship_map[j][i] == 2:          # catch if ship length is 2
                        ship_map[j][i] = chr(ship_count + 97)
                        ship_map[j][i+1] = chr(ship_count + 97)
                        ship_count += 1
                        continue
                    else:                       # catch if ship length is 3
                        print("current position HORIZ else exceptioned - make sure next print is == 3")
                        print(ship_map[j][i])
                        ship_map[j][i] = chr(ship_count + 97)
                        ship_map[j][i+1] = chr(ship_count + 97)
                        ship_map[j][i+2] = chr(ship_count + 97)
                        ship_count += 1
                        continue  
                elif j < len(ship_map) - 1 and ship_map[j+1][i] == ship_map[j][i]:    # the ship is horiz!
                    if ship_map[j][i] == 2:          # catch if ship length is 2
                        ship_map[j][i] = chr(ship_count + 97)
                        ship_map[j+1][i] = chr(ship_count + 97)
                        ship_count += 1
                        continue
                    else:                       # catch if ship length is 3
                        print("current position VERT else exceptioned - make sure next print is == 3")
                        print(ship_map[j][i])
                        ship_map[j][i] = chr(ship_count + 97)
                        ship_map[j+1][i] = chr(ship_count + 97)
                        ship_map[j+2][i] = chr(ship_count + 97)
                        ship_count += 1
                        continue    
                else:
                    print("parent comparitor else exceptioned - something went wrong")
                    print(ship_map[j][i], "j =", j, "i =", i)
    return ship_map, ship_count


def damaged_or_sunk(board, attacks):
    ship_map, ship_count = ship_identifier(board)
    aftermath_map, letters_hit, ship_map  = battle(ship_map, attacks)

    print("board, then aftermath_map, then letters_hit")
    print(board)
    print(aftermath_map, ship_count)                                 
    print(letters_hit)
    print(ship_map)
    
    sunk = 0
    damaged = 0
    not_touched = 0

    count = ship_count      # use Count as token for how many ships to attempt
    while count > 0:     # since Count == 0 when we're out of vessels, loop until it reaches 0
        break

    for j in range(len(aftermath_map)): # J = each position in "y" axis of Hits_map
        for i in range(len(aftermath_map[0])):  # I = each position in "x" axis of Hits_map
            if aftermath_map[j][i] == 0:
                continue
            
            print(f'j = {j}, i = {i}, value = {aftermath_map[j][i]}')

            # ok, so you found either a hit or a ship. Time to check
            # first check if ship length is 1 AND was hit
            if board[j][i] == 1 and aftermath_map[j][i] == "#":                 
                count -= 1  
                sunk += 1
                letters_hit.remove(ship_map[j][i])
                print('value was SINGLE')
                continue

            # if current value was hit AND in letters_hit, then it WASN'T sunk
            elif ship_map[j][i] in letters_hit and aftermath_map[j][i] == "#": 
                count -=1
                damaged += 1
                letters_hit.remove(ship_map[j][i])
                print('value was NOT SUNK')
                continue

            # count sunk vessels - because they were not found in aftermath_map,
            # then they were SUNK. Add remaining count in Letters_hit to Sunk
            else:
                print('exception caught')
                print(f'current value is {aftermath_map[j][i]} at position {j},{i}')
                continue
    sunk += len(letters_hit)
    count -= len(letters_hit)
    print(f'sunk = {sunk}, damaged = {damaged}, not_touched = {not_touched}')
    print(f'count = {count}')






            


         

board = [[0,0,0,2,2,0],
         [0,3,0,0,0,0],
         [0,3,0,1,0,0],
         [0,3,0,1,0,0]]

attacks = [[2, 1], [1, 3], [4, 2]] 

damaged_or_sunk(board, attacks)
# Expected result: { 'sunk': 0, 'damaged': 2 , 'not_touched': 1, 'points': 0 }













##
# cntr + r + e to run


##########
#
# any(3 in row for row in board) # checks if there's any 3 left on board
#

"""def identify_vessels(board):
    #converts board to board_status, which uses a unique letter for each vessel, starting with "a" == chr(97)
    ship_count = 0                 # ship_count will be flag to keep track of which unique character we're on
    print(board)
    print(len(board))
    for j in range(len(board)): # J = each position in "y" axis of board
        for i in range(len(board[0])):  # I = each position in "x" axis of board
            print(j,i, board[j][i])
            if board[j][i] == 0 or type(board[j][i]) == str: 
                continue                # if current position is 0 -empty-, or is a string, move on
            elif board[j][i] == 1:
                board[j][i] = chr(ship_count + 97) 
                ship_count += 1    # reassign current position to next unique char, in order
                continue                # with Unique_Identit = 0 giving chr(97) = "a"
            else:        
                # you just hit a spot that's not a string, 0, or 1! Time to check for where the rest of your ship is
                print("you just got a tricky one! next print statements will indicate board and current pos")
                print(board)
                print(j, i)
                print("current val: ", board[j][i])

                if board[j][i+1] == board[j][i]: # the space next to current one is the same! you have a streak going on
                    if board[j][i+1] == 2 # indicates you got a streak of length 2

                    if board[j][i+2] == board[j][i]: # indicates spot 3 spaces over is also the same - ship of length three"""
            
"""            if board[j][i] == 2:
                if board[j+1][i] == 2:
                    board[j][i] = chr(ship_count + 97)
                    board[j+1][i] = chr(ship_count + 97)
                    ship_count += 1
                    continue
                if board[j][i]"""

"""def identify_vessels(board):
    #converts board to board_status, which uses a unique letter for each vessel, starting with "a" == chr(97)
    ship_count = 0                 # ship_count will be flag to keep track of which unique character we're on
    val_flag = 0
    for j in range(len(board)): # J = each position in "y" axis of board
        for i in range(len(board[0])):  # I = each position in "x" axis of board
            print(j,i, board[j][i])
            if board[j][i] == 0 or type(board[j][i]) == str: 
                continue                # if current position is 0 -empty-, or is a string, move on
            elif board[j][i] == 1:
                board[j][i] = chr(ship_count + 97) 
                ship_count += 1    # reassign current position to next unique char, in order
                continue                # with Unique_Identit = 0 giving chr(97) = "a"
            elif val_flag != 0 and board[j][i] == val_flag: # indicates *immediately previous value* was the same
                if val_flag == 2:       # you just found a 2 length ship! (horiz)
                    board[j][i] = chr(ship_count + 97)
                    board[j][i-1] = chr(ship_count + 97)
                    ship_count += 1
                    val_flag = 0
                    continue
                else:                   # you just found a 3 length ship! (horiz)
                    print("val_flag else exceptioned - make sure next print is == 3")
                    print(val_flag)
                    board[j][i] = chr(ship_count + 97)
                    board[j][i-1] = chr(ship_count + 97)
                    board[j][i-2] = chr(ship_count + 97)
                    ship_count += 1
                    val_flag = 0
                    continue
            elif val_flag != 0 and ( board[j][i] == 1 or board[j][i] == 0 or type(board[j][i]) == str):
                # if val_flag has value, you *just* previously indexed a ship of len >1
                # if current space is either 1, 0, *or* a string, then check pos below previous position
                if board[j+1][i-1] == """