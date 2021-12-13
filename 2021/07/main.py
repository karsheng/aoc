def parseFile(path):
    with open(path) as f:        
        content = f.read()
        return content.splitlines()

def preprocess(data):
    return [int(i) for i in data[0].split(",")]

data = parseFile("./input.txt")
preprocessed = preprocess(data)

def count_crabs(data):
    crab_counts = {i: 0 for i in range(max(data) + 1)}
    for d in data:
        crab_counts[d] += 1
    return crab_counts

def solve(data, cost_func):
    crab_counts = count_crabs(data)
    dists = {pos: 0 for pos in crab_counts.keys()}

    for pos in crab_counts.keys():
        dist = 0
        for k, v in crab_counts.items():
            dist += cost_func(pos, k) * v
        dists[pos] = dist
    return min(dists.values())

def natural_num_sum(n):
    return n*(n+1)/2

print("q1", solve(preprocessed, lambda x, y: abs(x-y)))
print("q2", solve(preprocessed, lambda x, y: natural_num_sum(abs(x-y))))
