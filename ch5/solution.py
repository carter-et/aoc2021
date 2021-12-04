import numpy as np
import time as t


def main():
    startTime = t.time()
    filename = 'data.txt'
    # filename = 'test.txt'
    file = open('G:/Personal/python-projects/advent-of-coding/ch5/' + filename, 'r')
    Lines = file.readlines()

    gamma = ""
    epsilon = ""
    amt_of_ones = []
    index = 0

    for line in Lines:
        tmp = []
        line = line.strip()
        if(index == 0): #setup
            for ch in line:
                amt_of_ones.append(0)
            amt_of_ones = np.array(amt_of_ones)
            print('starting set is: ', amt_of_ones)
        for ch in line:
            tmp.append(int(ch))

        amt_of_ones = np.add(amt_of_ones, np.array(tmp))

        index += 1

    print(amt_of_ones, index / 2)

    for num in amt_of_ones:
        if(num > (index / 2)):
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    
    print(binaryToDecimal(gamma) * binaryToDecimal(epsilon))
    endTime = t.time()
    print(endTime - startTime)


def binaryToDecimal(n):
    return int(n,2)

if __name__ == "__main__":
    main()