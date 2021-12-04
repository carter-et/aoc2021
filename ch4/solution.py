filename = 'data.txt'
# filename = 'test.txt'
file = open('G:/Personal/python-projects/advent-of-coding/ch3/' + filename, 'r')
Lines = file.readlines()

depth = 0 #up/down
distance = 0 #forward
travel = 0 #X
aim = 0
temp = []
for line in Lines:
    temp = line.split(' ', 1)
    travel = int(temp[1])
    match temp[0]:
        case 'forward':
            distance += travel
            depth += (aim * travel)
        case 'up':
            # depth = depth - travel
            aim -= travel
        case 'down':
            # depth = depth + travel
            aim += travel
print(depth * distance)