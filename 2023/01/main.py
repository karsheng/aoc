import re


def parse(filename):
    with open(filename) as f:
        data = f.read().splitlines()

    return data


def find_calibration_value(line):
    nums_only = re.sub(r"[A-z]", "", line)
    first = int(nums_only[0])
    second = int(nums_only[-1])
    return int(f"{first}{second}")


def solve1(data):
    total = 0
    for line in data:
        total += find_calibration_value(line)
    return total


def solve2(data):
    mapper = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }

    total = 0
    for line in data:
        for num in mapper.keys():
            line = line.replace(num, str(mapper[num]))
        total += find_calibration_value(line)

    return total


if __name__ == "__main__":
    data = parse("input.txt")
    print("P1", solve1(data))
    print("P2", solve2(data))
