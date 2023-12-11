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


part1()