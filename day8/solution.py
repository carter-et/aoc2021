import time as time
import math

from collections import Counter

dataFile = "data.txt"
testFile = "test.txt"
TESTING_MODE = False

#  aaaa      0000
# b    c    1    2
# b    c    1    2
#  dddd      3333
# e    f    4    5
# e    f    4    5
#  gggg      6666

class Code:
    def __init__(self, cipher_in, cipher_out):
        self.map = [''] * 10
        self.map_lines = [''] * 7
    
        self.frequencies = Counter(cipher_in.strip().replace(' ', ''))
        
        self.cipher_in = cipher_in.strip().split()
        self.cipher_out = cipher_out.strip().split()

    def getSimpleAnswer(self):
        count = 0
        for cipher_text in self.cipher_out:
            if(len(cipher_text) == 2 
            or len(cipher_text) == 3
            or len(cipher_text) == 4
            or len(cipher_text) == 7):
                count += 1
        return count

    def getMapping(self):
        # map the guarantees (4/10)
        for cipher_text in self.cipher_in:
            if(len(cipher_text) == 2):
                self.map[1] = cipher_text 
            if(len(cipher_text) == 3):
                self.map[7] = cipher_text
            if(len(cipher_text) == 4):
                self.map[4] = cipher_text
            if(len(cipher_text) == 7):
                self.map[8] = cipher_text

        # find 'a' (1/7)
        self.map_lines[0] = self.charNotIn(self.map[7], self.map[1])
        # find 'b', find 'e', find 'f' (4/7)
        for i in 'abcdefg':
            if(self.frequencies[i] == 6):
                self.map_lines[1] = i
            if(self.frequencies[i] == 4):
                self.map_lines[4] = i
            if(self.frequencies[i] == 9):
                self.map_lines[5] = i

        # find which set is 9 and which set is 2 (6/10)
        for cipher_text in self.cipher_in:

            # 9 has 6 segments, and does not contain [4]
            if(len(cipher_text) == 6
            and self.map_lines[4] not in cipher_text):
                self.map[9] = cipher_text
            
            # 2 has 5 segments, and is the only that contains a [4]
            if(len(cipher_text) == 5
            and self.map_lines[4] in cipher_text):
                self.map[2] = cipher_text
            
        # we know sets 1, 2, 4, 7, 8, 9
        # we know char [0], [1], [4], [5]

        # find which char is line [3]
        for i in 'abcdefg':
            if(i not in self.map[7]
            and i in self.map[2]
            and i in self.map[4]):
                self.map_lines[3] = i

        # find which set is 0 (7/10)
        for cipher_text in self.cipher_in:
            # 0 has 6 segments, and not contain [3]
            if(len(cipher_text) == 6
            and self.map_lines[3] not in cipher_text):
                self.map[0] = cipher_text

        # there should only be 1 remaining item with length of 6, 6
        for cipher_text in self.cipher_in:
            if(len(cipher_text) == 6
            and cipher_text != self.map[0]
            and cipher_text != self.map[9]):
                self.map[6] = cipher_text
            
            # we know [1] and [4], so we know 3
            if(len(cipher_text) == 5
            and self.map_lines[1] not in cipher_text
            and self.map_lines[4] not in cipher_text):
                self.map[3] = cipher_text

        # now find the last one (5)
        for cipher_text in self.cipher_in:
            found = False
            for i in self.map:
                if cipher_text == i:
                    found = True
            if(not found):
                self.map[5] = cipher_text
        # we know all the sets!

    def getDecodedCount(self):
        print(self.map)

        count = ''
        for cipher_text in self.cipher_out:
            for decoded in self.map:
                if(''.join(sorted(cipher_text)) == ''.join(sorted(decoded))):
                    count += str(self.map.index(decoded))

        print(count)
        return int(count)

    def charNotIn(self, hasChar, compareTo):
        for char in hasChar:
            if(char not in compareTo):
                return char
        return -1 # we should never hit this line 

def part_one(data):
    unique_digits = 0

    for item in data:
        code = Code(item[0], item[1])
        unique_digits += code.getSimpleAnswer()

    print(unique_digits)

    return None

def part_two(data):
    total_sum = 0
    for item in data:
        code = Code(item[0], item[1])
        code.getMapping()
        total_sum += code.getDecodedCount()
    
    print(total_sum)

    return None

def processData(filename):
    filepath = 'G:/Personal/python-projects/advent-of-coding/day8/' + filename

    data = []
    with open(filepath, 'r') as f:
        for line in f:
            data.append(line.split('|'))
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