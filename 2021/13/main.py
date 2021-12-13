def parse_file(path):
  f = open(path, "r")
  return [x.strip() for x in f.readlines()]


def preprocess(data):
  i = data.index("")
  coords = { tuple(int(i) for i in e.split(",")) for e in data[:i] }
  instructions= [r.split()[2] for r in data[i+1:]]
  instructions = [i.split("=") for i in instructions]
  return coords, instructions

path = "./input.txt"
coords, instructions = preprocess(parse_file(path))

def fold(coords, axis, val):
  if axis == "y":
    fold_points = {(x, y) for (x, y) in coords if y > val}
    for (x, y) in fold_points:
      coords.remove((x,y))
      coords.add((x, y-2*(y-val)))  
  else:  
    fold_points = {(x, y) for (x, y) in coords if x > val}
    for (x, y) in fold_points:
          coords.remove((x,y))
          coords.add((x-2*(x-val), y))

  return coords

coords = fold(coords, instructions[0][0], int(instructions[0][1]))

print("q1", len(coords))

def solve_2(coords, instructions):
  for i in instructions:
    coords = fold(coords, i[0], int(i[1]))

  max_x = max([x for (x,y) in coords])
  max_y = max([y for (x,y) in coords])
  grid = [["." for x in range(max_x + 1)] for y in range(max_y + 1)]
  
  for (x, y) in coords:
    grid[y][x] = "#"

  for r in grid:
    print("".join(r)) 
  

coords, instructions = preprocess(parse_file(path))
solve_2(coords, instructions)