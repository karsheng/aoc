def parse_file(path):
  f = open(path, "r")
  return [x.strip() for x in f.readlines()]

def preprocess(data):
  # pad edges with 999
  grid = [[int(i) for i in r] for r in data]
  for i in range(len(grid)):
    grid[i].insert(0, 999)
    grid[i].append(999)
  pads = [999 for i in range(len(grid[0]))]
  grid.insert(0, pads)
  grid.append(pads)

  return grid

def flash(i, j, grid, flashed):
  neighbours = [
    (i+1, j),
    (i-1, j),
    (i, j+1),
    (i, j-1),
    (i+1, j+1),
    (i+1, j-1),
    (i-1, j+1),
    (i-1, j-1),
  ]
  if grid[i][j] > 9 and grid[i][j] < 999  and (i, j) not in flashed:
    grid[i][j] = 0
    flashed.add((i, j))
    for (x, y) in neighbours:
      if (x, y) not in flashed:
        grid[x][y] += 1
        flash(x, y, grid, flashed)      

  return grid

def move_step(grid):
  flashed = set()
  for i in range(1, len(grid)-1):
    for j in range(1, len(grid[0])-1):
      grid[i][j] += 1
  for i in range(1, len(grid)-1):
    for j in range(1, len(grid[0])-1):
      grid = flash(i, j, grid, flashed)

  return grid, flashed

def solve_1(grid, steps):
  flashes = 0
  for s in range(steps):
    grid, flashed = move_step(grid)
    flashes += len(flashed)
  return grid, flashes

grid = preprocess(parse_file("./input.txt"))

grid, flashes = solve_1(grid, 100)
print("q1", flashes)

grid = preprocess(parse_file("./input.txt"))

def solve_2(grid):
  all_flashes = (len(grid) - 2) * (len(grid[0]) - 2)
  total_flashes = 0 
  i = 0
  while all_flashes != total_flashes:  
    grid, flashes = move_step(grid)
    total_flashes = len(flashes)
    i += 1
  return i

print("q2", solve_2(grid))