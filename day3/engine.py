def part1():

    file = open("input.txt", "r")

    matrix = []

    for line in file:
        matrix.append(list(line.strip()))

    ROWS, COLS = len(matrix), len(matrix[0])

    running_sum = 0

    def check_adjacent(r, c):
        curr_sum = 0

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for add_r, add_c in directions:
            pass
            

        return curr_sum

    for r in range(ROWS):
        for c in range(COLS):
            letter = matrix[r][c]
            if not letter.isalnum() and letter != '.':
                running_sum += check_adjacent(r, c)
        

part1()

