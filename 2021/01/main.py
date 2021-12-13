import pandas as pd

def parseFile(path, *, as_list, parse_int):
    with open(path) as f:        
        content = f.read()
        if as_list:
            if parse_int:
                return list(map(int, content.splitlines()))
            
        return content


def day01_1(data):
    count = 0
    v_before = data[0]
    for i in data:
        count = count + 1 if i > v_before else count + 0
        v_before = i
    return count


def day01_2(data):
    s = pd.Series(data)
    return day01_1(s.rolling(3).sum().values)
    
data = parseFile("./input.txt", as_list=True, parse_int=True)
print("Q1", day01_1(data))

print("Q2", day01_2(data))
