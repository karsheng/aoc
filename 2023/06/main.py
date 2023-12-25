def parse(filename):
    with open(filename) as f:
        data = [l.split() for l in f.read().splitlines()]
        time = [int(i) for i in data[0][1:]]
        record = [int(i) for i in data[1][1:]]
    return time, record


def record_breaking_count(time, record):
    def get_distances(t):
        distances = []
        for speed in range(t):
            time_remaining = t - speed
            distances.append(speed * time_remaining)
        return distances

    count = 0
    distances = get_distances(time)
    for d in distances:
        count += d > record

    return count


if __name__ == "__main__":
    time, record = parse("input.txt")
    p1 = 1
    for i, t in enumerate(time):
        p1 *= record_breaking_count(t, record[i])

    print("P1:", p1)

    t2 = int("".join([str(t) for t in time]))
    r2 = int("".join([str(r) for r in record]))

    print("P2:", record_breaking_count(t2, r2))
