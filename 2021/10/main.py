def parseFile(path):
    with open(path) as f:        
        content = f.read()
        return content.splitlines()


data = parseFile("input.txt")    

brackets = {
    "[" : "]",
    "<" : ">",
    "(" : ")",
    "{" : "}"
}

brackets_reversed = { v: k for k, v in brackets.items()}

def check_syntax(line):
    stack = []
    for b in line:
        if b in brackets.keys():
            stack.append(b)
            continue
        ob = stack.pop()
        if ob != brackets_reversed[b]:
            return b, stack

    return None, stack

score_scheme = {
    ")" : 3,
    "]" : 57,
    "}" : 1197,
    ">" : 25137
}

def solve_1(data):
    score = 0
    for line in data:
        bad_bracket, _ = check_syntax(line)
        if bad_bracket:
            score += score_scheme[bad_bracket]

    return score


score_scheme_2 = {
    ")" : 1,
    "]" : 2,
    "}" : 3,
    ">" : 4
}

def solve_2(data):
    scores = []
    for line in data:
        bad_bracket, stack = check_syntax(line)
        if bad_bracket is None:
            scores.append(0)
            while len(stack) > 0:
                b = brackets[stack.pop()]
                scores[-1] = scores[-1] * 5 + score_scheme_2[b]
    mid = int(len(scores)/2)
    return sorted(scores)[mid]

print("q1", solve_1(data))
print("q2", solve_2(data))