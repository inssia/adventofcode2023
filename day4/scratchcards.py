import re

def part1():
    file = open("input.txt", "r")

    winning_nums = []
    has_nums = []

    for line in file:
        parts = line.split(':')
        nums = parts[1].split('|')

        win_string = nums[0].strip().split(' ')
        has_string = nums[1].strip().split(' ')

        win_set = set()
        for num in win_string:
            if num != '':
                win_set.add(int(num))

        winning_nums.append(win_set)

        has_list = []
        for num in has_string:
            if num != '':
                has_list.append(int(num))

        has_nums.append(has_list)

    running_total = 0

    for i in range(len(has_nums)):
        running_total += match_nums(winning_nums[i], has_nums[i])

    print(running_total)

def match_nums(winning_nums, has_nums):

    counter = 0
    
    for num in has_nums:
        if num in winning_nums:
            counter += 1

    if counter == 0:
        return 0
    
    return 2 ** (counter-1)


def part2():

    file = open("input.txt", "r")

    mapping = {}

    for line in file:
        line = re.sub('[^0-9 |]', '', line).strip()

        wins_and_count, has_nums = line.split('|')
        wins_and_count = wins_and_count.strip().split()
        has_nums = has_nums.strip().split()

        count = int(wins_and_count[0])
        wins = set(wins_and_count[1:])

        mapping[count] = [wins, has_nums, 1]

    running_sum = 0

    for count in mapping:
        running_sum += duplicate_and_count(mapping, count)

    print(running_sum)

def duplicate_and_count(mapping, count):

    winning_nums, has_nums, current_number = mapping[count]

    wins = 0

    for num in has_nums:
        if num in winning_nums:
            wins += 1

    card_deck = count
    while wins >= 0 and card_deck <= len(mapping):
        mapping[card_deck][2] += current_number
        wins -= 1 
        card_deck += 1


    return current_number



    

part1()
part2()