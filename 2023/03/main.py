def parse_grid(filename):
    grid = {}
    with open(filename) as f:
        data = f.read().splitlines()
        for y, line in enumerate(data):
            n = len(line)
            x = 0
            while x < n:
                char = line[x]
                if char != ".":
                    if not char.isnumeric():
                        grid[(x, y)] = char
                    else:
                        j = 1
                        while x + j < n:
                            if line[x + j].isnumeric():
                                j += 1
                            else:
                                break
                        grid[(x, y)] = int(line[x : x + j])
                        x += j - 1

                x += 1

    return grid


def get_adjacent_cells(cell, val):
    n = len(str(val))
    x, y = cell
    occupied_cells = {(x + i, y) for i in range(n)}
    adjacent_cells = set()
    for i in range(n):
        adjacent_cells.add((x + 1 + i, y))
        adjacent_cells.add((x - 1 + i, y))
        adjacent_cells.add((x + i, y + 1))
        adjacent_cells.add((x + i, y - 1))
        adjacent_cells.add((x + 1 + i, y + 1))
        adjacent_cells.add((x + 1 + i, y - 1))
        adjacent_cells.add((x - 1 + i, y + 1))
        adjacent_cells.add((x - 1 + i, y - 1))

    return adjacent_cells - occupied_cells


def solve1(grid):
    total = 0
    for cell, val in grid.items():
        if type(val) == int:
            adjacent_cells = get_adjacent_cells(cell, val)
            for adjacent_cell in adjacent_cells:
                if adjacent_cell in grid:
                    total += val

    return total


def solve2(grid):
    total = 0
    cell_with_numbers = {}
    for (x, y), val in grid.items():
        if type(val) == int:
            n = len(str(val))
            for i in range(n):
                for i in range(n):
                    cell_with_numbers[(x + i, y)] = val

    for cell, val in grid.items():
        if val == "*":
            adjacent_cells = get_adjacent_cells(cell, val)
            overlapped_cells = adjacent_cells.intersection(
                set(cell_with_numbers.keys())
            )
            parts_no = {cell_with_numbers[cell] for cell in overlapped_cells}

            val = 1
            if len(parts_no) == 2:
                for part in parts_no:
                    val *= part
                total += val

    return total


if __name__ == "__main__":
    grid = parse_grid("input.txt")
    print("P1", solve1(grid))
    print("P2", solve2(grid))
