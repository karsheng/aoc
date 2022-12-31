def parse(filename):
    with open(filename) as f:
        data = f.read().splitlines()
        data.append('')

    return data


filename = "input.txt"
data = parse(filename)

def solve(data):
    top_three = [0, 0, 0]
    i = 0
    current_val = 0

    while i < len(data):
        val = data[i]
        if len(val) > 0:
            current_val += int(val)
        else:
            top_three.append(current_val)
            top_three = sorted(top_three, reverse=True)
            top_three.pop()
            current_val = 0

        i += 1
    return top_three


print("Part1 :", solve(data)[0])
print("Part2 :", sum(solve(data)))

