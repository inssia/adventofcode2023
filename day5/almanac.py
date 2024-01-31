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

    seed_ranges = []

    file[0] = file[0].replace("seeds: ", "").strip().split()

    for i in range(0, len(file[0]), 2):
        seed_ranges.append([int(file[0][i]), int(file[0][i]) + int(file[0][i+1])])


    # format: [[[dest_start, source_start, step], ...], ...]
    mapped_ranges = []

    for i in range(1, len(file)):
        curr_ranges = []
        rows = file[i].split('\n')

        for row in rows:
            if "map" not in row:
                curr_ranges.append([int(x) for x in row.split()])

        mapped_ranges.append(curr_ranges)

    print(find_lowest_location_from_seed_ranges(seed_ranges, mapped_ranges))

def find_lowest_location_from_seed_ranges(seed_ranges, mapped_ranges):
    
    for map_range in mapped_ranges:
        new_seed_ranges = []
        while len(seed_ranges) > 0:
            start, end = seed_ranges.pop(0)
            translate_mappings(start, end, map_range, new_seed_ranges)

        seed_ranges = new_seed_ranges

def translate_mappings(seed_start, seed_end, map_ranges, new_seed_ranges):

    print(seed_start, seed_end, new_seed_ranges, map_ranges)

    for range_dest_start, range_src_start, range_step in map_ranges:
        pass

    
    


part2()