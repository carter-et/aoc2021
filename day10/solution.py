import time as time

dataFile = "data.txt"
testFile = "test.txt"
TESTING_MODE = False

PARANTHESIS_ERROR = 3
BRACKET_ERROR = 57
SQUIGLY_ERROR = 1197
ARROW_ERROR = 25137

PARANTHESIS_SCORE = 1
BRACKET_SCORE = 2
SQUIGLY_SCORE = 3
ARROW_SCORE = 4

def part_one(filename):
    openers = '([{<'
    closers = ')]}>'
    expectations = []
    error_score = 0

    filepath = 'G:/Personal/python-projects/advent-of-coding/day10/' + filename

    with open(filepath, 'r') as f:
        for line in f:

            for char in line.strip():
                if(char in openers):
                    expectations.append(getCloser(char))
                if(char in closers):
                    expectation = expectations.pop()
                    if(not meetsExpectation(char, expectation)):
                        error_score += getErrorScore(char)
                        print('line was corrupted')
                        break
            
    print(error_score)

def part_two(filename):
    openers = '([{<'
    closers = ')]}>'
    scores = []

    filepath = 'G:/Personal/python-projects/advent-of-coding/day10/' + filename

    with open(filepath, 'r') as f:
        for line in f:
            expectations = []
            corrupted = False
            for char in line.strip():
                if(char in openers):
                    expectations.append(getCloser(char))
                if(char in closers):
                    expectation = expectations.pop()
                    if(not meetsExpectation(char, expectation)):
                        print('line was corrupted')
                        corrupted = True
                        break
            if(not corrupted):
                scores.append(processRemainers(expectations))
    
    scores.sort()
    print(scores.pop(int((len(scores) - 1)/2)))

def getCloser(char):
    openers = ['(','[','{','<']
    closers = [')',']','}','>']
    return closers[openers.index(char)]

def meetsExpectation(char, expectations):
    closers = [')',']','}','>']
    return closers.index(char) == closers.index(expectations)

def getErrorScore(char):
    if(char == ')'):
        return PARANTHESIS_ERROR
    if(char == ']'):
        return BRACKET_ERROR
    if(char == '}'):
        return SQUIGLY_ERROR
    if(char == '>'):
        return ARROW_ERROR
    
    print('we should never make it here.')
    return 0

def getRemainerScore(char):
    if(char == ')'):
        return PARANTHESIS_SCORE
    if(char == ']'):
        return BRACKET_SCORE
    if(char == '}'):
        return SQUIGLY_SCORE
    if(char == '>'):
        return ARROW_SCORE
    
    print('we should never make it here.')
    return 0

def processRemainers(remainers):
    score = 0
    remainers.reverse()
    for remainer in remainers:
        score = (score * 5) + getRemainerScore(remainer)
    return score

if __name__ == "__main__":
    filename = dataFile
    if(TESTING_MODE):
        filename = testFile


    s_time = time.time()
    # part_one(filename)
    part_two(filename)
    e_time = time.time()

    print('Time: ', e_time - s_time)