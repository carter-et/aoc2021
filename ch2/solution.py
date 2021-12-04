file = open('G:/Personal/python-projects/advent-of-coding/ch2/data.txt', 'r')
Lines = file.readlines()

prev_lines = []
prev_sum = 0
curr_sum = 0
count = 0
index = 0

for line in Lines:
    line = int(line)
    prev_lines.append(line)
    curr_sum = curr_sum + line
    if index > 2:
        curr_sum = curr_sum - prev_lines[index-3]
        if curr_sum > prev_sum:
            count += 1
    prev_sum = curr_sum
    index = index + 1

print(count)