import time as time
import numpy as np

# PARTS
def part_one(coordinate_data, size):
    board = createBoard(size)

    for coordinates in coordinate_data:
        board = drawLine(board, coordinates)

    # print(board)
    print('# over overlapping zones', calculateBoard(board))

    return None

def part_two():
    # lol never used this.
    return None

#HELPERS
def intepret_data():
    # filename = 'test.txt'
    filename = 'data.txt'
    filepath = 'G:/Personal/python-projects/advent-of-coding/day5/' + filename
    print('---------------------------------------------------------')
    print(filepath)
    print('---------------------------------------------------------')

    coordinate_data = []
    largest_number = 0

    with open(filepath, 'r') as f:
        for line in f:
            this_max = extractMaximum(line)
            if(largest_number < this_max):
                largest_number = this_max
            coordinate_data.append(processCoordinates(line))
    
    # print(coordinate_data)
    # print(largest_number)

    return (coordinate_data, largest_number)

def processCoordinates(line):
    coordinate_sets = []
    for set in line.split('->'):
        set = set.strip().split(',')
        coordinate_sets.append([int(set[0]), int(set[1])])
    
    return coordinate_sets

def createBoard(size):
    size += 1 #size is given to us, starting at 0
    return np.zeros((size, size))
# only draws vertical lines
def drawLine(board, coordinates):
    # print(coordinates)
    # fun fact: because it's a sqaure, as long as we are consistent, what is x and what is y doesn't matter.
    set1 = np.array(coordinates[0])
    set2 = np.array(coordinates[1])
    line = np.subtract(set2, set1)
    # print(set1, set2)
    # print(line)

    # we are only considering lines that are horizontal or vertical
    if(len(line[np.where(line == 0)]) == 1): 
        # print(set1, set2)
        # print(line)

        # starting coords
        sx = set1[0]
        sy = set1[1]
        # ending coords
        ex = set2[0]
        ey = set2[1]
        # indeces
        x = sx
        y = sy

        # do x row
        while(x != ex):
            board[x][sy] += 1
            if(ex > sx):
                x += 1
            if(ex < sx):
                x -= 1
            if(ex == x):
                board[x][sy] += 1
    
        # do y row
        while(y != ey):
            board[sx][y] += 1
            if(ey > sy):
                y += 1
            if(ey < sy):
                y -= 1
            if(ey == y):
                board[sx][y] += 1
    if(abs(line[0]) == abs(line[1])):
        # starting coords
        sx = set1[0]
        sy = set1[1]
        # ending coords
        ex = set2[0]
        ey = set2[1]
        # indeces
        x = sx
        y = sy

        while(x != ex and y != ey):
            board[x][y] += 1
            if(ex > sx):
                x += 1
            if(ex < sx):
                x -= 1
            if(ey > sy):
                y += 1
            if(ey < sy):
                y -= 1
            if(ex == x and ey == y):
                board[x][y] += 1

    # print(board)
    # print(board.transpose())
    # print()
    return board

def calculateBoard(board):
    return len(board[np.where(board > 1)])
# https://www.geeksforgeeks.org/extract-maximum-numeric-value-given-string/
def extractMaximum(ss):
    num, res = 0, 0
      
    # start traversing the given string 
    for i in range(len(ss)):
          
        if ss[i] >= "0" and ss[i] <= "9":
            num = num * 10 + int(int(ss[i]) - 0)
        else:
            res = max(res, num)
            num = 0
          
    return max(res, num)

#MAIN
if __name__ == "__main__":
    s_time = time.time()
    (coordinate_data, size) = intepret_data()
    part_one(coordinate_data, size)
    e_time = time.time()
    print('Time: ', e_time - s_time)