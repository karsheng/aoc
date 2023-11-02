def parse(filename):
    with open(filename) as f:
        data = f.read().splitlines()

    return data


filename = "input.txt"
data = parse(filename)

mapper = {chr(i): i - 96 for i in range(97, 97 + 26)}

mapper.update({chr(i): i - 65 + 27 for i in range(65, 65 + 26)})


def solve1(data, mapper):
    score = 0

    for line in data:
        h = len(line) // 2
        first = set(line[:h])
        second = set(line[h:])

        common = first.intersection(second)
        for common_char in common:
            score += mapper[common_char]

    return score


def solve2(data, mapper):
    score = 0
    n = len(data)

    for i in range(0, n, 3):
        lines = [set(line) for line in data[i : i + 3]]
        common = lines[0].intersection(lines[1]).intersection(lines[2])
        for common_char in common:
            score += mapper[common_char]

    return score


print("Part1 :", solve1(data, mapper))
print("Part2 :", solve2(data, mapper))
