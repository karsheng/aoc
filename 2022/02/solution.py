def parse(filename):
    with open(filename) as f:
        data = f.read().splitlines()

    return data


filename = "input.txt"
data = parse(filename)

mapper1 = {
    "A": {
        "X": 1 + 3,
        "Y": 2 + 6,
        "Z": 3,
    },
    "B": {
        "X": 1,
        "Y": 2 + 3,
        "Z": 3 + 6,
    },
    "C": {
        "X": 1 + 6,
        "Y": 2,
        "Z": 3 + 3,
    }
}

mapper2 = {
    "A": {
        "X": 0 + 3,
        "Y": 3 + 1,
        "Z": 6 + 2,
    },
    "B": {
        "X": 0 + 1,
        "Y": 3 + 2,
        "Z": 6 + 3,
    },
    "C": {
        "X": 0 + 2,
        "Y": 3 + 3,
        "Z": 6 + 1,
    }
}

def solve(data, mapper):
    score = 0
    for d in data:
        a, b = d.split(" ")
        score += mapper[a][b]

    return score


print("Part1 :", solve(data, mapper1))
print("Part2 :", solve(data, mapper2))

