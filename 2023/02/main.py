def parse(filename):
    with open(filename) as f:
        data = f.read().splitlines()

    return data


def solve(data):
    limits = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    total = 0
    impossible_games = set()
    for line in data:
        splits = line.split(":")
        id = int(splits[0][5:])
        draws = splits[1].split(";")

        color_count = {"red": 0, "green": 0, "blue": 0}

        for draw in draws:
            balls = draw.strip().split(",")
            for ball in balls:
                ball_splits = ball.strip().split(" ")
                count = int(ball_splits[0])
                color = ball_splits[1]
                if int(count) > limits[color]:
                    impossible_games.add(id)

                if color_count[color] < count:
                    color_count[color] = count

        total += color_count["red"] * color_count["green"] * color_count["blue"]

    part1 = sum(i for i in range(1, len(data) + 1) if i not in impossible_games)
    part2 = total
    return part1, part2


if __name__ == "__main__":
    data = parse("input.txt")
    part1, part2 = solve(data)
    print("P1", part1)
    print("P2", part2)
