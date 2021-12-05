import time as time
import board as b

def part_one(bingo_calls, boards):
    print('running part one...')
    hasWon = False
    score = 0
    for call in bingo_calls:
        for board in boards:
            (hasWon, score) = board.calculateBoard(call)
            if(hasWon):
                print(score)
                print(call)
                print('there was a winner. score: ', score * call)
                return None

def part_two(bingo_calls, boards):
    print('running part two...')
    print(bingo_calls)
    print('amount of boards: ', len(boards))

    hasWon = False
    score = 0
    for call in bingo_calls:
        print('calling out number: ', call)
        for board in boards:
            (hasWon, score) = board.calculateBoard(call)
            if(hasWon):
                print('winner with score of: ', score, call, score * call)
        
#read data and return a tuple
def intepret_data():
    # filename = 'test.txt'
    # filename = 'test2.txt'
    # filename = 'test3.txt'
    filename = 'data.txt'
    filepath = 'G:/Personal/python-projects/advent-of-coding/day4/' + filename
    print('---------------------------------------------------------')
    print(filepath)
    print('---------------------------------------------------------')

    bingo_calls = ""
    boards = []
    isCallsFlag = True

    with open(filepath, 'r') as f:
        temp_board = []
        temp_index = 0
        for line in f:
            if(isCallsFlag):
                bingo_calls = list(map(int, line.strip().split(',')))
                isCallsFlag = False
            else:
                if(line != '\n'):
                    tmp = list(map(int, line.strip().split()))
                    temp_board.append(tmp)
                    temp_index += 1
                    if(temp_index == 5):
                        boards.append(b.Board(temp_board))
                        temp_board = []
                        temp_index = 0

    return (bingo_calls, boards)

if __name__ == "__main__":
    (bingo_calls, boards) = intepret_data()
    part_one(bingo_calls, boards)
    part_two(bingo_calls, boards)
    