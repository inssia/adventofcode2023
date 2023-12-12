import re

def part1():
    file = open("input.txt", "r").read().strip().split('\n\n')

    seed_nums = [int(x) for x in re.sub("seeds: ", "", file[0]).split()]

    # format: [[[dest_start, source_start, step], ...], ...]
    mapped_ranges = []

    for i in range(1, len(file)):
        curr_ranges = []
        rows = file[i].split('\n')

        for row in rows:
            if "map" not in row:
                curr_ranges.append([int(x) for x in row.split()])

        mapped_ranges.append(curr_ranges)

    print(find_lowest_location(seed_nums, mapped_ranges))

def find_lowest_location(seed_nums, mapped_ranges):

    for i in range(len(seed_nums)):
        for map_range in mapped_ranges:
            for dest_start, source_start, step in map_range:
                if seed_nums[i] >= source_start and seed_nums[i] < source_start + step:
                    seed_nums[i] = dest_start+(seed_nums[i]-source_start)
                    break

    return min(seed_nums)

part1()

def part2():
    file = open("input.txt", "r").read().strip().split('\n\n')

    seed_ranges = [int(x) for x in re.sub("seeds: ", "", file[0]).split()]

    # format: [[[dest_start, source_start, step], ...], ...]
    mapped_ranges = []

    for i in range(1, len(file)):
        curr_ranges = []
        rows = file[i].split('\n')

        for row in rows:
            if "map" not in row:
                curr_ranges.append([int(x) for x in row.split()])

        mapped_ranges.append(curr_ranges)

    print(find_lowest_location_from_ranges(seed_ranges, mapped_ranges))

def find_lowest_location_from_ranges(seed_ranges, mapped_ranges):

    for i in range(0, len(seed_ranges), 2):
        for map_range in mapped_ranges:
    
            pass


part2()