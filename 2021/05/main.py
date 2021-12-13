def parseFile(path):
    with open(path) as f:        
        content = f.read()
        return content.splitlines()


def preprocess(data):
    coords = []
    for r in data:
        fr, _, to = r.split()
        x1, y1 = (int(i) for i in fr.split(","))
        x2, y2 = (int(i) for i in to.split(","))
        coords.append((x1,y1,x2,y2))
    return coords

def generate_points_covered(x1,y1,x2,y2):
    points_covered = set()
    step_x = 1 if x1 < x2 else -1
    step_y = 1 if y1 < y2 else -1
    x = x1
    y = y1
    while x != x2 or y != y2:
        points_covered.add((x,y))
        x = x + step_x if x != x2 else x
        y = y + step_y if y != y2 else y
    points_covered.add((x,y))
    return points_covered
def two_lines_overlapped(data, h_and_v=True):
    points = {}
    for d in data:
        x1,y1,x2,y2 = d
        if h_and_v:
            if x1 == x2 or y1 == y2:
                points_covered = generate_points_covered(x1,y1,x2,y2)
            else:
                points_covered = {}
        else:
            points_covered = generate_points_covered(x1,y1,x2,y2)

        for pt in points_covered:
            if pt in points.keys():
                points[pt] += 1
            else:
                points[pt] = 1
    at_least_two = [k for k, val in points.items() if val > 1]
    return len(at_least_two)

data = parseFile("./input.txt")
processed = preprocess(data)
print("q1", two_lines_overlapped(processed))

print("q2", two_lines_overlapped(processed, h_and_v=False))

