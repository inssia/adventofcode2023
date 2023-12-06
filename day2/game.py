import re
def part1():
    file = open("input.txt", "r")

    running_sum = 0

    for line in file:
        full_line = line.split(':')
        game_number = full_line[0]
        line_game_rounds = full_line[1]

        game_rounds = line_game_rounds.split(';')

        game_number = re.sub("[^0-9]", "", game_number)
        game_number = int(game_number)
        
        if isvalid(game_rounds):
            running_sum += game_number

    print(running_sum)

# only 12 red cubes, 13 green cubes, and 14 blue cubes

def isvalid(array_of_rounds):
    for round in array_of_rounds:
        cubes = round.split(',')

        sum_of_colours = 0
        
        for colour in cubes:

            number =  int(re.sub("[^0-9]", "", colour))
            sum_of_colours += number

            if 'red' in colour and number > 12:
                return False
            
            if 'green' in colour and number > 13:
                return False
            
            if 'blue' in colour and number > 14:
                return False
        
        if sum_of_colours > 39:
            return False
        
    return True            

part1()

def part2():
    
    file = open("input.txt", "r")

    running_sum = 0

    for line in file:
        full_line = line.split(':')
        full_game_rounds = full_line[1]
        game_rounds = full_game_rounds.split(';')

        running_sum += calculate_power(game_rounds)

    print(running_sum)

def calculate_power(array_of_rounds):

    min_cubes = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    for round in array_of_rounds:
        round = round.split(',')

        for each_colour in round:
            array = each_colour.strip().split(' ')
            num = int(array[0])
            cube_colour = array[1]

            min_cubes[cube_colour] = max(min_cubes[cube_colour], num)

    product = 1

    for i in min_cubes.values():
        product *= i
            
    return product     

part2()