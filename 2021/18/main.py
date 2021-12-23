import ast
from typing import List


def process_list(pairs):
    return ast.literal_eval(pairs)

pairs = "[[[[[9,8],1],2],3],4]"
pairs = "[[[[0    ,9],2],3],4]"

pairs2 = "[7,[6,[5,[4,[3,2]]]]]"
pairs2 = "[7,[6,[5,[7,0    ]]]]"

pairs3 = "[[6,[5,[4,[3,2]]]],1]"
pairs3 = "[[6,[5,[7,0    ]]],3]"

pairs4 = "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"
pairs4 = "[[3,[2,[8,0    ]]],[9,[5,[7,0    ]]]]"

def explode(pairs: str):
    stack = []
    numbers = {}
    exploding_pair = []
    exploded = False
    explode_right = None
    explode_left = None
    reconstruct = {}
    
    for i, c in enumerate(pairs):
        reconstruct[i] = c

        if c == "[":
            stack.append(c)

        if c.isnumeric():
            print(numbers)
            if len(stack) > 4:
                exploding_pair.append(int(c))
            elif exploded:
                val = int(c) + explode_right
                numbers[i] = val
                reconstruct[i] = str(val)
                exploded = False
            else:
                numbers[i] = int(c)

        if c == "]":
            stack.pop()
            if exploded:
                reconstruct[i] = ""
                reconstruct[i-1] = ""
                reconstruct[i-2] = ""
                reconstruct[i-3] = ""
                reconstruct[i-4] = "0"
                

        if len(exploding_pair) == 2:
            explode_right = exploding_pair.pop()
            explode_left = exploding_pair.pop()
            if len(numbers) > 0:
                idx = max(numbers.keys())
                numbers[idx] += explode_left
                reconstruct[idx] = str(numbers[idx]) 

            numbers[i] = 0
            exploded = True

    s = ""
    for i in range(len(pairs)):
        if len(reconstruct[i]) > 0:
            s += reconstruct[i] 


    return s


pair5 = "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"
s = explode(pairs3)

print(s)
