import time as time

dataFile = "data.txt"
testFile = "test.txt"
TESTING_MODE = False

class Octopus:
    def __init__(self, flash_val):
        self.flash_val = flash_val
        self.neighbors = []
        self.hasFlashed = False

    def setNeighbors(self, neighbors):
        self.neighbors = neighbors

    def inc(self):
        self.flash_val += 1
    
    def check_if_flashed(self):
        flashes = 0
        if(self.flash_val > 9 and not self.hasFlashed):
            self.hasFlashed = True
            for octopus in self.neighbors:
                octopus.inc()
                flashes += octopus.check_if_flashed()
            return flashes + 1 # include this item as having flashed
            
        return flashes

    def reset(self):
        if(self.hasFlashed):
            self.flash_val = 0
        self.hasFlashed = False

def part_one(octopuses):
    flashes = 0
    for step in range(100):
        print('day: ', step, 'flashes: ', flashes)
        for octo in octopuses:
            octo.inc()
        for octo in octopuses:
            flashes += octo.check_if_flashed()
        for octo in octopuses:
            octo.reset()
    
    print('flashes', flashes)

def part_two(octopuses):
    day = 1
    while(True):
        flashes = 0
        for octo in octopuses:
            octo.inc()
        for octo in octopuses:
            flashes += octo.check_if_flashed()
        for octo in octopuses:
            octo.reset()

        if(flashes == 100):
            print('day', day)
            break

        day += 1

def processData(filepath):
    filepath = 'G:/Personal/python-projects/advent-of-coding/day11/' + filename

    octopuses = []

    with open(filepath, 'r') as f:
        for line in f:
            for num in line.strip():
                octopuses.append(Octopus(int(num)))
    
    # this part is kinda wonky. because we know the dimensions, we can use the position in the array to get "neighbors"
    index = 0
    for octopus in octopuses:
        # nw, n, ne, w, e, sw, s, se
        neighbors = []

        if(index < 10): # top row
            if(index == 0): #left side
                neighbors = [
                    octopuses[index+1],
                    octopuses[index+10],
                    octopuses[index+11]
                ]
            elif(index == 9): # right side
                neighbors = [
                    octopuses[index-1],
                    octopuses[index+9],
                    octopuses[index+10],
                ]
            else: # anywhere in the middle
                neighbors = [
                    octopuses[index-1],
                    octopuses[index+1],
                    octopuses[index+9],
                    octopuses[index+10],
                    octopuses[index+11]
                ]
        elif(index >= 90): # bottom row
            if(index % 10 == 0): #left side
                neighbors = [
                    octopuses[index-10],
                    octopuses[index-9],
                    octopuses[index+1],
                ]
            elif(index % 10 == 9): # right side
                neighbors = [
                    octopuses[index-11],
                    octopuses[index-10],
                    octopuses[index-1],
                ]
            else: # anywhere in the middle
                neighbors = [
                    octopuses[index-11],
                    octopuses[index-10],
                    octopuses[index-9],
                    octopuses[index-1],
                    octopuses[index+1],
                ]
        else: # anywhere inbetween
            if(index % 10 == 0): #left side
                neighbors = [
                    octopuses[index-10],
                    octopuses[index-9],
                    octopuses[index+1],
                    octopuses[index+10],
                    octopuses[index+11]
                ]
            elif(index % 10 == 9): # right side
                neighbors = [
                    octopuses[index-11],
                    octopuses[index-10],
                    octopuses[index-1],
                    octopuses[index+9],
                    octopuses[index+10],
                ]
            else: # anywhere in the middle
                neighbors = [
                    octopuses[index-11],
                    octopuses[index-10],
                    octopuses[index-9],
                    octopuses[index-1],
                    octopuses[index+1],
                    octopuses[index+9],
                    octopuses[index+10],
                    octopuses[index+11]
                ]
        octopus.setNeighbors(neighbors)
        index+=1

    return octopuses

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