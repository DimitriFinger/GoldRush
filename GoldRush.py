

def no_memory_recursion(matrix, miner_x, miner_y, gold_bag): 
    print("valor gold_bar: " + str(gold_bag))
    print("posição minerador: " + str(miner_x), str(miner_y))
    print("gold na posição: " + str(matrix[miner_x][miner_y]))

    if miner_x == 0 and miner_y == len(matrix) - 1:
        print(gold_bag)

    if miner_x > 0 and matrix[miner_x-1][miner_y] != 'x':
        north = matrix[miner_x-1][miner_y]
        #gold_bag += int(matrix[miner_x - 1][miner_y])
        #miner_x = miner_x -1
    else:
        north = -1000

    if miner_y <len(matrix)-1 and miner_y+1 != 'x':
        east = matrix[miner_x][miner_y+1]
        #gold_bag += int(matrix[miner_x - 1][miner_y])
        #miner_y = miner_y +1
    else:
        east = -1000

    if miner_x > 0 and miner_y < len(matrix)-1 and matrix[miner_x-1][miner_y+1] != 'x':
        northeast = matrix[miner_x-1][miner_y+1]
        #gold_bag += int(matrix[miner_x - 1][miner_y])
        #miner_x = miner_x -1
    else:
        northeast= -1000
    

    if int(north) > int(east) and int(north) > int(northeast):
        gold_bag += int(north)
        miner_x = miner_x -1        
    elif int(east) > int(north) and int(east) > int(northeast):
        miner_y = miner_y + 1
        gold_bag += int(east)
    else:
        miner_x = miner_x - 1
        miner_y = miner_y + 1
        gold_bag += int(northeast)

    print(north,east,northeast)
    print(miner_x,miner_y)
    print(gold_bag)
    
    #no_memory_recursion(matrix,miner_x,miner_y,gold_bag)


  
    #for n in range(len(matrix)): print(matrix[n])




if __name__ == "__main__":

    arq = open('caso10.txt', 'r') # choose test file
    line = []
    matrix = []
    text = arq.readlines()
    line = text[1:]
    
    # uncomment both lines below to print matrix
    #for i in range(len(line)): matrix.append(line[i].replace('\n', ''))       
    #for i in range(len(line)): print(matrix[i])

    matrix = []
    for n in range(len(line)): matrix.append(line[n].split())

     
    miner_x = len(matrix) - 1 
    miner_y = 0
    gold_bag = -5
    #no_memory_recursion(matrix, miner_x, miner_y, gold_bag)

    print(matrix[9][0])
    print(len(matrix))