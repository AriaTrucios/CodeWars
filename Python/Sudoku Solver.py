"""Write a function that will solve a 9x9 Sudoku puzzle. The function will take one argument consisting of the 
2D puzzle array, with the value 0 representing an unknown square.

The Sudokus tested against your function will be "easy" (i.e. determinable; there will be no need to assume and test possibilities on unknowns) 
and can be solved with a brute-force approach."""
def sudoku(puzzle, x=0, y=0):
    x,y = find_next_empty_cell(puzzle)
    if x == -1 and y == -1: # If Find_Next_Empty_Cell returns a value equivalent to boolean False for x and y, the puzzle is solved!
        return True
    for val in range(1,10):
        if check_if_valid_entry(puzzle, x, y, val): # continues if Check_If_Valid_Entry returns True
            puzzle[x][y] = val
            if sudoku(puzzle, x, y):
                return puzzle
            # Undo the current cell for backgracking
            puzzle[x][y] = 0
    return False

def find_next_empty_cell(puzzle): # finds the 'next' cell with value 0 and outputs its position i,j
    for x in range(9):
        for y in range(9):
            if puzzle[x][y] == 0:
                return x,y
    return -1,-1


def check_if_valid_entry(puzzle, x, y, val):
    # Check row for validity
    for i in range(9):
        if puzzle[x][i] == val and y != i:
            return False

    # Check column for validity
    for i in range(9):
        if puzzle[i][y] == val and x != i:
            return False
    
    # Check 3x3 square surrounding current cell
    box_pos_X, box_pos_Y = 3 * (x // 3) , 3 * (y // 3)
    for i in range(box_pos_X, box_pos_X + 3):
        for j in range(box_pos_Y, box_pos_Y + 3):
            if puzzle[i][j] == val and (i, j) != (x, y):
                return False
    
    return True







"""soduku=[[7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]]"""

#this bricks
"""soduku=[[5,0,0,0,9,7,0,0,0],
[0,1,0,8,0,0,2,0,0],
[0,7,9,2,0,0,0,1,0],
[0,0,0,0,0,0,4,0,8],
[3,0,0,0,0,0,0,0,1],
[9,0,1,0,0,0,0,0,0],
[0,6,0,0,0,8,1,5,0],
[0,0,5,0,0,1,0,6,0],
[0,0,0,7,6,0,0,0,3]]"""

#medium
soduku=[[0,7,5,0,0,0,4,0,6],
[0,0,0,7,0,0,2,1,8],
[0,4,0,1,0,0,7,0,0],
[7,0,6,0,0,9,0,0,0],
[0,5,0,0,0,8,0,6,2],
[0,0,0,0,0,0,0,0,4],
[0,0,0,0,0,0,8,2,7],
[0,0,3,2,5,0,6,0,9],
[6,2,0,0,0,0,5,0,0]]

#hard
"""soduku=[[0,0,0,0,0,0,0,3,0],
[1,0,5,0,0,0,0,4,0],
[3,0,0,2,0,9,6,5,0],
[7,5,3,0,0,0,0,1,0],
[0,0,0,0,6,3,0,0,0],
[0,9,0,5,0,0,0,0,0],
[0,0,0,0,9,5,0,0,0],
[0,3,1,7,2,0,0,0,4],
[0,4,9,0,1,0,5,0,0]]"""

#expert
"""
soduku=[[0,7,0,0,2,0,5,1,0],
[0,0,0,0,0,0,0,0,2],
[0,6,0,0,0,0,3,0,7],
[5,0,0,0,7,0,0,4,0],
[0,0,9,0,0,0,2,0,5],
[8,0,0,5,0,0,6,0,0],
[0,1,0,3,9,6,0,0,0],
[0,0,0,0,0,0,0,0,0],
[7,0,0,0,0,0,0,0,9]]
"""
#blank sample
"""soduku=[[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0]]"""

solve(soduku)
print("--------------------------------------------------")