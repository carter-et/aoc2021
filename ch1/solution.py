def run():
    file = open('./ch1/test.txt', 'r')
    Lines = file.readlines()

    prev_line = 0
    count = 0
    index = 0
    for line in Lines:
        if index > 0:
            if prev_line < line:
                count += 1
        prev_line = line
        index = index + 1
    print(count)
    return count

if __name__ == "__main__":
    run()