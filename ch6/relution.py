import numpy as np
import time as time

OXY = True
CO2 = False

def main():
    startTime = time.time()
    filename = 'data.txt'
    # filename = 'test.txt'
    file = open('G:/Personal/python-projects/advent-of-coding/ch6/' + filename, 'r')
    Lines = file.readlines()

    #scope variables
    gamma_arr = getBitCriteria(Lines, OXY)
    epsilon_arr = getBitCriteria(Lines, CO2)
    co2 = getRating(Lines, epsilon_arr, 0, CO2)
    oxy = getRating(Lines, gamma_arr, 0, OXY)
    
    print('life support rating: ', (binaryToDecimal(oxy) * binaryToDecimal(co2)))
    endTime = time.time()
    print(endTime - startTime)

def getRating(Lines, arr, depth, type):
    if(len(Lines) == 1):
        return Lines[0]
    else:
        #filter lines
        bit_criterion = arr[depth]
        Lines = filterByCriteria(Lines, bit_criterion, depth)

        tmp_arr = getBitCriteria(Lines, type)
        return getRating(Lines, tmp_arr, depth+1, type)

def filterByCriteria(Lines, bit_criterion, depth):
    tmp_Lines = []
    for line in Lines:
        line = line.strip()
        compareBit = line[depth:(depth + 1)]
        if(meetsCriteria(compareBit, bit_criterion)):
            tmp_Lines.append(line)
    return tmp_Lines

def getBitCriteria(Lines, type):
    #get new bit criteria
    amt_of_ones = []
    index = 0
    tmp_arr = []

    for line in Lines:
        tmp = []
        line = line.strip()

        if(index == 0): #setup
            for ch in line:
                amt_of_ones.append(0)
            amt_of_ones = np.array(amt_of_ones)

        for ch in line:
            tmp.append(int(ch))
        amt_of_ones = np.add(amt_of_ones, np.array(tmp))
        index += 1
    
    for num in amt_of_ones:
        if(type): #is OXY
            if(num >= (index / 2)):
                tmp_arr.append(1)
            else:
                tmp_arr.append(0)
        else: #is CO2
            if(num >= (index / 2)):
                tmp_arr.append(0)
            else:
                tmp_arr.append(1)
    
    return tmp_arr

def meetsCriteria(compare, to):
    return (int(compare) == int(to))

def binaryToDecimal(n):
    return int(n,2)

if __name__ == "__main__":