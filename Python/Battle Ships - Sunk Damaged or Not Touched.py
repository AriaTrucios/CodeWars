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

def battle(map, attacks): 
    ships_hit = []
    for i in attacks:
        x_pos = i[0] - 1
        y_pos = len(map) - i[1]
        if map[y_pos][x_pos] == 0:
            continue
        else:
            if map[y_pos][x_pos] not in ships_hit:
                ships_hit.append(map[y_pos][x_pos])
            map[y_pos][x_pos] = "#" # use "#" to indicate hits_map
            continue
    return map, ships_hit


def ship_identifier(map):
    #converts map to ship_map, which uses a unique letter for each vessel, starting with "a" == chr(97)
    ship_map = [row[:] for row in map]
    
    # total_ship_list will be list of every ship on map 
    # (used to keep count of total ships for scorekeeping)
    total_ship_list = []
    [[total_ship_list.append(i) for i in row if i != 0 and i not in total_ship_list] for row in ship_map]
    total_ship_list.sort()                  
    return ship_map, total_ship_list



def damaged_or_sunk(board, attacks):
    ship_map, total_ship_list = ship_identifier(board)
    aftermath_map, ships_hit  = battle(ship_map, attacks)

    # use Board for the virgin board
    # use Aftermath_Map for board with "#" for hits
    
    sunk = 0
    damaged = 0
    not_touched = 0

    for j in range(len(aftermath_map)): # J = each position in "y" axis of Hits_map
        for i in range(len(aftermath_map[0])):  # I = each position in "x" axis of Hits_map
            if aftermath_map[j][i] == 0:
                continue

            # if you got a hit, check what ship it belongs to, and if all instances of it are # on this map
            # AND check to be sure it's on Ships_Hit, as if it's not, then we've checked it already!
            if aftermath_map[j][i] == "#" and board[j][i] in ships_hit:    

                # if number of ship is ANYWHERE on Aftermath_Map, then it wasn't sunk!
                if any(board[j][i] in x for x in aftermath_map):
                    damaged += 1
                    ships_hit.remove(board[j][i])
                    continue
                
                # if above wasn't caught, then it WAS completely sunk!
                else:
                    sunk += 1
                    ships_hit.remove(board[j][i])
                    continue
            
    not_touched = len(total_ship_list) - sunk - damaged

    answer = {
        'sunk' : sunk,
        'damaged' : damaged,
        'not_touched' : not_touched,
        'points' : calculate_score(sunk, damaged, not_touched)
    }

    return answer
            

         
board = [[0,0,0,2,2,0],
         [0,3,0,0,0,0],
         [0,3,0,1,0,0],
         [0,3,0,1,0,0]]

attacks = [[2, 1], [1, 3], [4, 2]] 

damaged_or_sunk(board, attacks)
# Expected result: { 'sunk': 0, 'damaged': 2 , 'not_touched': 1, 'points': 0 }


"""
from collections import Counter

def damaged_or_sunk(board, attacks):
    # Invert board and shift attacks to 0 based indexcing
    board = board[::-1]
    attacks = [(r-1, c-1) for r, c in attacks]
    # Quantify initial state
    start_ships = Counter(v for r in board for v in r)
    # Apply attacks
    for r, c in attacks:
        board[c][r] = "X"
    # Quantify end state
    end_ships = Counter(v for r in board for v in r)
    # Analyse change in state
    sunk, damaged, not_touched = 0, 0, 0
    for id, count in start_ships.items():
        if id != 0:
            if end_ships[id] == count:
                not_touched += 1
            elif end_ships[id] == 0:
                sunk += 1
            else:
                damaged += 1
    score = sunk + 0.5 * damaged - not_touched
    return {'sunk': sunk, 'damaged': damaged, 'not_touched': not_touched, 'points': score}
____________________________________________________________________________

class CoastGuard:
    def __init__(self, board):
        self.board = board
        self.score = { 'sunk': 0, 'damaged': 0 , 'not_touched': 0, 'points': 0}
        self.boats = {
            1: [],
            2: [],
            3: []
        }
        self.boatHits = {}
        self.activateBoatRadar()
    def activateBoatRadar(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                boat_number = self.board[i][j]
                if boat_number > 0:
                    self.boats[boat_number].append([i,j])
        for boat in self.boats:
            if len(self.boats[boat]) > 0:
                self.boatHits[boat] = []
    def calculate_score(self):
        for boat in self.boatHits:
            if len(self.boatHits[boat]) == len(self.boats[boat]):
                self.score['sunk'] += 1
                self.score['points'] += 1
            elif len(self.boatHits[boat]) == 0:
                self.score['not_touched'] += 1
                self.score['points'] -= 1
            else:
                self.score['damaged'] += 1
                self.score['points'] += 0.5
        return self.score
                
    def damage(self, index_coords, boat):
        print(index_coords)
        self.boatHits[boat].append(index_coords)
        return

def damaged_or_sunk (board, attacks):
    coast_guard = CoastGuard(board)
    for attack in attacks:
        translation = translate(*attack)
        boat_number = board[translation[0]][translation[1]]
        if boat_number > 0:
            coast_guard.damage(translation, boat_number)
    return coast_guard.calculate_score()
    
def translate(x,y):
    return [-y, x-1]
"""

