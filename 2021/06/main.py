def parseFile(path):
    with open(path) as f:        
        content = f.read()
        return content.splitlines()

def preprocess(data):
    return [int(i) for i in data[0].split(",")]

data = parseFile("./input.txt")
preprocessed = preprocess(data)

def lantern_fish(data, day):
    fishes = {i:0 for i in range(9)}
    for d in data:
        fishes[d] += 1

    for i in range(day):
        zeros = fishes[0]
        old_fishes = fishes.copy()
        for j in range(8, 0, -1):
            fishes[j-1] = old_fishes[j]
        fishes[6] += zeros
        fishes[8] = zeros

    return sum(fishes.values())
print("q1", lantern_fish(preprocessed, 80))
print("q2", lantern_fish(preprocessed, 256))