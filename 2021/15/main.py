from heapq import heappush, heappop

def parse_file(path):
    with open(path) as f:        
        content = f.read()
        return content.splitlines()

def preprocess(data):
    grid = {}
    for i in range(len(data)):
        for j in range(len(data[0])):
            grid[(i, j)] = int(data[i][j])
    return grid

def grid_dijkstra(grid, start):
    dist = { square: float("infinity") for square in grid.keys() }
    dist[start] = 0

    Q = [(0, start)]

    while len(Q) > 0:
        current_dist, current_square = heappop(Q)

        if current_dist > dist[current_square]:
            continue
        x, y = current_square
        neighbours = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        for neighbour in neighbours:
            if neighbour in grid.keys():
                d = current_dist + grid[neighbour]

                if d < dist[neighbour]:
                    dist[neighbour] = d
                    heappush(Q, (d, neighbour))

    
    return dist


data = parse_file("input.txt")
grid = preprocess(data)
dist = grid_dijkstra(grid, (0,0))
end = (len(data) - 1, len(data[0])-1)
print("q1", dist[end])

def expand_grid(data, times):
    grid = preprocess(data)
    new_grid = grid.copy()
    for n1 in range(times):
        for n2 in range(times):
            for (x, y), risk_level in grid.items():
                new_x = x + n1 * len(data)
                new_y = y + n2 * len(data[0])
                new_risk_level = risk_level + n1 + n2
                new_grid[new_x, new_y] =  new_risk_level if new_risk_level < 10 else new_risk_level % 9 

    return new_grid

times = 5
expanded_grid = expand_grid(data, times)
dist = grid_dijkstra(expanded_grid, (0,0))
end = (len(data)*times - 1, len(data[0]) * times -1)
print("q2", dist[end])
