def parse(filename):
    with open(filename) as f:
        data = f.read().splitlines()

        seeds = [int(i) for i in data[0][7:].split()]
        map_str = data[2:]
        mapper = []
        temp = None
        for line in map_str:
            if "map" in line:
                temp = []
            elif line == "":
                mapper.append(temp)
                temp = []
            else:
                d = [int(i) for i in line.split()]
                d += [range(d[1], d[1] + d[2])]
                d += [range(d[0], d[0] + d[2])]
                temp.append(d)

        mapper.append(temp)
    return seeds, mapper


def solve1(seeds, mapper):
    def get_next_item(item, maps):
        for map in maps:
            if item in map[3]:
                return item - map[1] + map[0]
        return item

    min_loc = float("inf")

    for seed in seeds:
        item = seed
        for maps in mapper:
            item = get_next_item(item, maps)

        min_loc = min(min_loc, item)

    return min_loc


def generate_all_seeds(seeds):
    n = len(seeds) // 2
    all_seeds = []
    for i in range(n):
        seed = seeds[i * 2]
        l = seeds[i * 2 + 1]
        all_seeds.append(range(seed, seed + l))

    return all_seeds


def solve2(all_seeds, mapper):
    def get_prev_item(item, maps):
        for map in maps:
            if item in map[4]:
                return item - map[0] + map[1]
        return item

    item = 0
    rev_mapper = mapper[::-1]
    while True:
        prev_item = item
        for maps in rev_mapper:
            prev_item = get_prev_item(prev_item, maps)

        for seeds in all_seeds:
            if prev_item in seeds:
                return item

        item += 1


if __name__ == "__main__":
    seeds, mapper = parse("input.txt")
    min_loc = solve1(seeds, mapper)
    print("P1:", min_loc)

    all_seeds = generate_all_seeds(seeds)
    min_loc = solve2(all_seeds, mapper)
    print("P2:", min_loc)
