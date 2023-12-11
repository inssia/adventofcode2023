def part1():

    file = open("input.txt", "r")

    matrix = []

    for line in file:
        matrix.append(list(line.strip()))

    ROWS, COLS = len(matrix), len(matrix[0])

    running_sum = 0

    for r in range(ROWS):
        for c in range(COLS):
            letter = matrix[r][c]
            if not letter.isnumeric() and letter != '.':
                running_sum += check_adjacent(matrix, r, c)

    print(running_sum)

def check_adjacent(matrix, r, c):
    curr_sum = 0

    directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for add_r, add_c in directions:
        new_r, new_c = r+add_r, c+add_c
        if matrix[new_r][new_c].isnumeric():
            curr_sum += extract_number(matrix, new_r, new_c)       

    return curr_sum

def extract_number(matrix, r, c):
        
        COLS = len(matrix[0])

        number_list = []

        curr_c = c

        while curr_c >= 0 and matrix[r][curr_c].isnumeric():
            curr_c -= 1

        curr_c += 1

        while curr_c < COLS and matrix[r][curr_c].isnumeric():
            number_list.append(matrix[r][curr_c])
            matrix[r][curr_c] = '.'
            curr_c += 1

        number = int(''.join(number_list))

        return number   

def part2():

    file = open("input.txt", "r")

    matrix = []

    for line in file:
        matrix.append(list(line.strip()))

    ROWS, COLS = len(matrix), len(matrix[0])

    running_sum = 0

    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == '*':
                running_sum += check_gear_ratio(matrix, r, c)

    print(running_sum)

def check_gear_ratio(matrix, r, c):

    counter = 0
    
    curr_product = 1

    directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for add_r, add_c in directions:
        new_r, new_c = r+add_r, c+add_c
        if matrix[new_r][new_c].isnumeric():
            curr_product *= extract_number(matrix, new_r, new_c)       
            counter += 1

    if counter == 2:
        return curr_product
    else:
        return 0

    

    

part1()
part2()
