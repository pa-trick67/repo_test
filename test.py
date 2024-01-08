import os
os.system('cls')

width = 4
height = 4
matrix_bool= [
    [True,True,False,True],
    [True,False,True,True],
    [False,True,False,True],
    [True,True,True,False]
]
matrix = [
    ["0 0","1 0","-1 -1","3 0"],
    ["0 1","-1 -1","2 1","3 1"],
    ["-1 -1","1 2","-1 -1","3 2"],
    ["0 3","1 3","2 3","-1 -1"]
]

for y in range(height):
    for x in range(width):    
        # Cell
        cell = matrix[y][x]
            
        # Cell_right
        
        if x+1 == width:
            cell_right = "-1 -1"
        else:
            cell_right = matrix[y][x+1]
            
        # Cell_bottom
        if y+1 == height:
            cell_bottom = "-1 -1"
        else:
            cell_bottom = matrix[y+1][x]
            
        result = cell + " " + cell_right + " " + cell_bottom
        if matrix_bool[y][x]: 
            print(result)

        
