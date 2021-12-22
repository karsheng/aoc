from collections import namedtuple
from typing import Tuple

def parse_file(path):
    with open(path) as f:        
        content = f.read()
        return content.splitlines()

Target = namedtuple("Target", ["area", "x_max", "x_min", "y_max", "y_min"])

def preprocess(data):
    splits = data.split()[2:]
    x = splits[0][2:].split(".")
    y = splits[1][2:].split(".")
    x_min, x_max = int(x[0]), int(x[2][:-1])
    y_min, y_max = int(y[0]), int(y[2])
    
    return x_min, x_max, y_min, y_max

class Probe:
    def __init__(self, x, y, vx, vy, target: Target):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.target = target

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.vx -= self.vx/abs(self.vx) if self.vx != 0 else 0
        self.vy -= 1
        
    def is_short(self):
        return self.vx == 0 and self.x < self.target.x_min

    def within_limit(self):
        return self.x <= self.target.x_max and self.y >= self.target.y_min

    def on_target(self):
        return (self.x, self.y) in self.target.area



x_min, x_max, y_min, y_max = preprocess(parse_file("./input.txt")[0])

area = { (x, y) for y in range(y_min, y_max + 1) for x in range(x_min, x_max + 1) }
target = Target(area, x_max, x_min, y_max, y_min)

def solve(target: Target):
    max_height = 0
    distinct_velocities = set()
    for vx in range(1, target.x_max + 1):
        vy = target.y_min
        while vy < abs(target.y_min):
            y_max = 0
            probe = Probe(0, 0, vx, vy, target)
            while probe.within_limit():
                probe.move()
                y_max = max(y_max, probe.y)
                if probe.on_target():
                    max_height = max(max_height, y_max)
                    distinct_velocities.add((vx, vy))
                    break
                    
            if probe.is_short():
                break
            vy += 1

    return max_height, distinct_velocities

max_height, distinct_velocities = solve(target)
print("q1", max_height)
print("q2", len(distinct_velocities))
