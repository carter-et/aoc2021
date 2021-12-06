import time as time

raw_data = [1,1,3,1,3,2,1,3,1,1,3,1,1,2,1,3,1,1,3,5,1,1,1,3,1,2,1,1,1,1,4,4,1,2,1,2,1,1,1,5,3,2,1,5,2,5,3,3,2,2,5,4,1,1,4,4,1,1,1,1,1,1,5,1,2,4,3,2,2,2,2,1,4,1,1,5,1,3,4,4,1,1,3,3,5,5,3,1,3,3,3,1,4,2,2,1,3,4,1,4,3,3,2,3,1,1,1,5,3,1,4,2,2,3,1,3,1,2,3,3,1,4,2,2,4,1,3,1,1,1,1,1,2,1,3,3,1,2,1,1,3,4,1,1,1,1,5,1,1,5,1,1,1,4,1,5,3,1,1,3,2,1,1,3,1,1,1,5,4,3,3,5,1,3,4,3,3,1,4,4,1,2,1,1,2,1,1,1,2,1,1,1,1,1,5,1,1,2,1,5,2,1,1,2,3,2,3,1,3,1,1,1,5,1,1,2,1,1,1,1,3,4,5,3,1,4,1,1,4,1,4,1,1,1,4,5,1,1,1,4,1,3,2,2,1,1,2,3,1,4,3,5,1,5,1,1,4,5,5,1,1,3,3,1,1,1,1,5,5,3,3,2,4,1,1,1,1,1,5,1,1,2,5,5,4,2,4,4,1,1,3,3,1,5,1,1,1,1,1,1]
raw_test = [3,4,3,1,2]
TESTING_MODE = False
DAYS = 256

class Fish:
    def __init__(self, ttl):
        self.ttl = ttl
    
    def decreaseTTL(self):
        if(self.ttl == 0):
            self.ttl = 6
            return True
        self.ttl -= 1
        return False

def part_one(data, days):
    fish_list = []
    # create the initial list of fish
    for fish_ttl in data:
        fish_list.append(Fish(fish_ttl))

    for day in range(days):
        new_fish_list = []
        for fish in fish_list:
            if(fish.decreaseTTL()):
                new_fish_list.append(Fish(8))
        fish_list.extend(new_fish_list)
        # print('Day: ', day, ' State: ', fish_list)
        print('Day: ', day)
        print('New fish: ', len(new_fish_list))
    
    print('Total fish: ', len(fish_list))
    return None

def part_two(data, days):
    # initialize rollig list
    rolling_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for item in data:
        rolling_list[item] += 1

    print('rolling list: ', rolling_list)

    # run each day
    for day in range(days):
        tmp = rolling_list[0]
        rolling_list[0] = rolling_list[1]
        rolling_list[1] = rolling_list[2]
        rolling_list[2] = rolling_list[3]
        rolling_list[3] = rolling_list[4]
        rolling_list[4] = rolling_list[5]
        rolling_list[5] = rolling_list[6]
        rolling_list[6] = rolling_list[7]
        rolling_list[7] = rolling_list[8]
        rolling_list[8] = 0
        rolling_list[6] += tmp # old fish go back into circulation 
        rolling_list[8] += tmp # for every old fish there is a new fish

        # print('Day: ', day + 1)
        # print('New fish: ', rolling_list[7])

    print('Total Fish: ', sum(rolling_list))

    return None

if __name__ == "__main__":

    raw = raw_data
    if(TESTING_MODE):
        raw = raw_test
        # DAYS = 18

    s_time = time.time()

    # part_one(raw, DAYS)
    
    part_two(raw, DAYS)

    e_time = time.time()

    print('Time: ', e_time - s_time)