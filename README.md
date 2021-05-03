# GoldRush


Requirements

Numpy package - Install using "pip install numpy" at bash


  
    if matrix[miner_x-1][miner_y] == 'x' or miner_x == 0:
        north = -100
    else:
        north = int(matrix[miner_x-1][miner_y])


    if miner_y < len(matrix):
        if not matrix[miner_x][miner_y + 1]:
            east = -100
        else:
            east = int(matrix[miner_x][miner_y + 1])




    if matrix[miner_x - 1][miner_y + 1] == 'x' or miner_x == len(matrix) or miner_y == len(matrix)-1:
            northeast = -100
    else:   
        northeast = int(matrix[miner_x-1][miner_y+1])

    #if matrix[miner_x-1][miner_y] != 'x':
    #    north = int(matrix[miner_x-1][miner_y])
    #    print(north)


    if north > east and north > northeast:
        gold_bag += north
        miner_x = miner_x -1        
    elif east > north and east > northeast:
        miner_y = miner_y + 1
        gold_bag += east
    else:
        miner_x = miner_x - 1
        miner_y = miner_y + 1
        gold_bag += northeast

    print(north,east,northeast)

    if miner_x == 0 and miner_y == len(matrix):
        print(gold_bag)
    else:
        no_memory_recursion(matrix,miner_x, miner_y,gold_bag)
