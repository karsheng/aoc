
def parseFile(path, ):
    with open(path) as f:        
        content = f.read()
        return content.splitlines()
            

def preprocess(el):
    direction, value = el.split()
    return direction, int(value)

def countPosAndDepth(input_data):
    position = 0
    depth = 0
    for direction, value in input_data:
        position = position + value if direction == "forward" else position
        
        if direction == "down":
            depth += value 
        elif direction == "up":
            depth -= value
    return position, depth

data = parseFile("./input.txt")


preprocessed = [preprocess(d) for d in data]
position, depth = countPosAndDepth(preprocessed)

print("q1", position * depth)


def count_pos_depth_aim(input_data):
    position = 0
    depth = 0
    aim = 0
    for direction, value in input_data:        
        if direction == "down":
            aim += value
        elif direction == "up":
            aim -= value
        elif direction == "forward":
            position += value
            depth += aim * value
    return position, depth

position, depth = count_pos_depth_aim(preprocessed)
print("q2", position * depth)


