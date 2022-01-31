import time as time

dataFile = "data.txt"
testFile = "test.txt"
TESTING_MODE = True

def part_one(data):
    print(data)

    pass

def part_two(data):
    pass

def processData(filepath):
    filepath = 'G:/Personal/python-projects/advent-of-coding/day12/' + filename

    data = []

    with open(filepath, 'r') as f:
        for line in f:
            (from_val, to_val) = line.strip().split('-')

            if(str(from_val) != 'start' and str(to_val) != 'end'): 
                data.append([from_val, to_val])
                data.append([to_val, from_val])
            else:
                data.append([from_val, to_val])

    return convert(data)

def convert(arr):
    paths_dict = {}
        
    return 

if __name__ == "__main__":
    filename = dataFile
    if(TESTING_MODE):
        filename = testFile

    data = processData(filename)

    s_time = time.time()
    part_one(data)
    # part_two(data)
    e_time = time.time()

    print('Time: ', e_time - s_time)