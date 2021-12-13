def parseFile(path):
    with open(path) as f:        
        content = f.read()
        return content.splitlines()

def preprocess(data):
    parsed = [[int(i) for i in d] for d in data]
    # pad the edges with high values
    for r in parsed:
        r.insert(0, 999)
        r.append(999)
    
    top_bottom = [999 for i in range(len(parsed[0]))]
    parsed.insert(0, top_bottom)
    parsed.append(top_bottom)  
    return parsed

def get_low_points(preprocessed):
    low_points = []
    for i in range(1, len(preprocessed)-1):
        for j in range(1, len(preprocessed[0])-1):
            combination = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
            smallest_neighbour = min([preprocessed[x][y] for x, y in combination])
            if preprocessed[i][j] < smallest_neighbour:
                low_points.append((i, j))               
    return low_points

def solve_1(preprocessed):
    low_points = get_low_points(preprocessed)
    total = 0
    for i, j in low_points:
        total += preprocessed[i][j] + 1
    return total

def get_incremental_neighbours(i: int, j: int, preprocessed: list, neighbour_set: set):
    v = preprocessed[i][j]
    combination = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
    for x, y in combination:
        if preprocessed[x][y] < 9 and (x, y) not in neighbour_set:
            neighbour_set.add((x,y))
            get_incremental_neighbours(x, y, preprocessed, neighbour_set)

    return neighbour_set

def solve_2(preprocessed):
    low_points = get_low_points(preprocessed)
    basins = []
    for index, (i, j) in enumerate(low_points):
        incremental_neighbours = get_incremental_neighbours(i, j, preprocessed, set())
        no_of_basins = len(incremental_neighbours)
        basins.append(no_of_basins)
    largest = sorted(basins)[-3:]
    return largest[0] * largest[1] * largest[2]

from time import perf_counter as pfc

start = pfc()
data = parseFile("./input.txt")
preprocessed = preprocess(data)
print("q1", solve_1(preprocessed))
print("q2", solve_2(preprocessed))
print(pfc()-start)