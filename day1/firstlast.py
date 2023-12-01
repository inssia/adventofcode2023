import re
def part1():
    file = open("input.txt", "r")

    running_sum = 0

    for line in file:
        nums = re.sub("[^0-9]", "", line)
        first_last = int(nums[0]+nums[-1])
        running_sum += first_last

    print(running_sum)

def part2():
    file = open("input.txt", "r")

    running_sum = 0

    mapping = {
        "one": '1',
        "two": '2',
        "three": '3', 
        "four": '4', 
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9'
    }


    for line in file:
        nums = []
        for index in range(len(line)):

            if line[index].isnumeric():
                nums.append(line[index])

            else:
                for word in mapping:
                    if line[index:].startswith(word):
                        nums.append(mapping[word])

        firstlast = int(nums[0] + nums[-1])
        running_sum += firstlast

    print(running_sum)

part1()
part2()