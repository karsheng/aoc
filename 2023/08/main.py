import math


def parse(filename):
    with open(filename) as f:
        data = f.read().splitlines()
        instruction = data[0]
        nodes = {}
        for d in data[2:]:
            l = d.split("=")
            key = l[0].strip()
            val = l[1].replace(" ", "")[1:-1].split(",")
            nodes[key] = val
    return instruction, nodes


def solve(instruction, nodes, starting_node, end):
    instr = [0 if i == "L" else 1 for i in instruction]
    steps = 0
    current_node = starting_node
    while True:
        for i in instr:
            steps += 1
            current_node = nodes[current_node][i]

            if current_node.endswith(end):
                return steps


if __name__ == "__main__":
    instruction, nodes = parse("input.txt")
    print("P1:", solve(instruction, nodes, "AAA", "ZZZ"))
    starting_nodes = {k: k for k in nodes.keys() if k[2] == "A"}

    p2 = 1
    for node in starting_nodes:
        p2 = math.lcm(p2, solve(instruction, nodes, node, "Z"))

    print("P2:", p2)
