import time as time
import sys

sys.setrecursionlimit(10**6)

dataFile = "data.txt"
testFile = "test.txt"
TESTING_MODE = False

def part_one(data):
    lows = getLows(data)
    print(sum(lows))
    return None

def part_two(_2d_array):
    basin_sizes = []
    skip_list = []
    # check each board position
    for i in range(len(_2d_array)):
        for j in range(len(_2d_array[i])):
            curr = _2d_array[i][j]
            basin = []
            if(curr != 9 and (i, j) not in skip_list):
                (basin, skip_list) = getBasinAndSkipList(i, j, _2d_array, skip_list)
                basin_sizes.append(len(basin))

    sum = 1
    top3 = sorted(basin_sizes, reverse=True)[:3]
    for basin_size in top3:
        sum = sum * basin_size

    print(sum)
    return None

def getBasinAndSkipList(i, j, arr, skip_list):
    basin = []
    if(arr[i][j] != 9 and (i, j) not in skip_list):
        basin = recursiveSearch(i, j, arr, basin)
    skip_list += basin
    
    return (basin, skip_list)

def recursiveSearch(i, j, arr, basin):
    curr = arr[i][j]
    if(curr == 9):
        return basin

    if(curr != 9 and (i, j) not in basin):
        basin.append((i, j))

        if(getNorth(i, j, arr) != 9):
            basin = recursiveSearch(i - 1, j, arr, basin)
        if(getSouth(i, j, arr) != 9):
             basin = recursiveSearch(i + 1, j, arr, basin)
        if(getWest(i, j, arr) != 9):
             basin = recursiveSearch(i, j - 1, arr, basin)
        if(getEast(i, j, arr) != 9):
             basin = recursiveSearch(i, j + 1, arr, basin)
    return basin

def getLows(_2d_array):
    lows = []
    for i in range(len(_2d_array)):
        for j in range(len(_2d_array[i])):
            curr = _2d_array[i][j]
            north= getNorth(i, j, _2d_array)
            east= getEast(i, j, _2d_array)
            south= getSouth(i, j, _2d_array)
            west= getWest(i, j, _2d_array)
            comparison = [north, south, west, east]

            if(all(k > curr for k in comparison)):
                lows.append(curr + 1)

    print(lows)
    return lows

def getNorth(i, j, arr):
    if(i == 0):
        return 9
    else: return arr[i-1][j]

def getWest(i, j, arr):
    if(j == 0):
        return 9
    else: return arr[i][j-1]

def getSouth(i, j, arr):
    if(i+1 == len(arr)):
        return 9
    else: return arr[i + 1][j]

def getEast(i, j, arr):
    if(j+1 == len(arr[i])):
        return 9
    else: return arr[i][j+1]

def processData(filename):
    filepath = 'G:/Personal/python-projects/advent-of-coding/day9/' + filename

    data = []
    with open(filepath, 'r') as f:
        for line in f:
            data.append([int(x) for x in str(line.strip())])

    return data

if __name__ == "__main__":
    filename = dataFile
    if(TESTING_MODE):
        filename = testFile

    data = processData(filename)

    s_time = time.time()
    # part_one(data)
    part_two(data)
    e_time = time.time()

    print('Time: ', e_time - s_time)