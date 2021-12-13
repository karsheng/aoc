
def parseFile(path):
    with open(path) as f:        
        content = f.read()
        return content.splitlines()
def preprocess(data):
    patterns = []
    outputs = []
    for r in data:
        pattern, output = r.split("|")
        patterns.append(pattern.split())
        outputs.append(output.split())
    return patterns, outputs

data = parseFile("./input.txt")
patterns, outputs = preprocess(data)

pattern_count = {
    2: 1,
    3: 7,
    4: 4,
    7: 8,

}

def solve_1(outputs, pattern_count):
    instances = 0
    for out in outputs:
        lens = [pattern_count.get(len(i), 0) != 0  for i in out]
        instances += sum(lens)
    return instances

print("q1", solve_1(outputs, pattern_count))

def find_pattern_one_matching(pattern_one, patterns, intersects):
    for i in patterns:

        if len(set(pattern_one).intersection(set(i))) == intersects:
            return i

def find_5_9(len_fives, len_sixes):
    for lf in len_fives:
        for ls in len_sixes:
            slf = set(lf)
            sls = set(ls)
            if len(slf.intersection(sls)) == 5:
                return lf, ls

def build_dict(pattern, pattern_count):
    # find 1, 4, 7, 8
    pattern_dict = {i: pattern_count.get(len(i))for i in pattern}
    value_dict = { v: k for k, v in pattern_dict.items()}

    # find 3
    pattern_one = value_dict[1]
    len_fives = [i for i in pattern if len(i) == 5]
    pattern_3 = find_pattern_one_matching(pattern_one, len_fives, 2)
    pattern_dict[pattern_3] = 3
    len_fives = [i for i in len_fives if i != pattern_3] # update len_fives

    # find 6
    len_sixes = [i for i in pattern if len(i) == 6]
    pattern_6 = find_pattern_one_matching(pattern_one, len_sixes, 1)
    pattern_dict[pattern_6] = 6
    len_sixes = [i for i in len_sixes if i != pattern_6] # update len_sixes

    # find 5, 9
    pattern_5, pattern_9 = find_5_9(len_fives, len_sixes)
    pattern_dict[pattern_5] = 5
    pattern_dict[pattern_9] = 9

    # find 0, 2
    pattern_0 = [i for i in len_sixes if i != pattern_9][0]
    pattern_2 = [i for i in len_fives if i != pattern_5][0]

    pattern_dict[pattern_0] = 0
    pattern_dict[pattern_2] = 2

    return pattern_dict


def solve_2(patterns, outputs, pattern_count):
    total = 0
    for i in range(len(patterns)):
        pattern = patterns[i]
        output = outputs[i]
        pattern_dict = build_dict(pattern, pattern_count)
        sorted_pattern_dict = {"".join(sorted(k)): v for k, v in pattern_dict.items()}
        vals = int("".join([str(sorted_pattern_dict["".join(sorted(o))]) for o in output]))
        print(vals)
        total += vals

    return total

print("q2", solve_2(patterns, outputs, pattern_count))

