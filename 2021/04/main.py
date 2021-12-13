def parseFile(path):
    with open(path) as f:        
        content = f.read()
        return content.splitlines()

def parse_boards(data):
    boards = []
    for i in range(0, len(data), 6):
        board = []
        for j in range(i, i+5):
            board.append([int(k) for k in data[j].split()])
            
        boards.append(board)

    return boards

class BingoBoard():
    def __init__(self, board):
        self.board = board
        self.height = len(board)
        self.width = len(board[0])
        self.state = [[False for i in r] for r in board] 
        self.loc = {}
        for i in range(self.width):
            for j in range(self.height):
                self.loc[self.board[i][j]] = i, j
    
    def update(self, n):
        if n in self.loc.keys():
            i, j = self.loc[n]
            self.state[i][j] = True
        
    def win_check(self):
        return self.check_cols() or self.check_rows()

    @property
    def unchecked_nums(self):
        unchecked = []
        for i in range(self.width):
            for j in range(self.height):
                if self.state[i][j] == False:
                    unchecked.append(self.board[i][j])
        return unchecked

    def check_cols(self):
        for i in range(len(self.state)):
            col = []
            for j in range(len(self.state[i])):
                 col.append(self.state[j][i])
            if all(col):
                return True
        return False

    def check_rows(self):
        for r in self.state:
            if all(r):
                return True
        return False

    def print_state(self):
        for r in self.state:
            print(r)
    
def bingo(numbers, boards):
    bingo_boards = [BingoBoard(board) for board in boards]
    i = 0
    while i < len(numbers):
        n = numbers[i]
        for bingo_board in bingo_boards:
            bingo_board.update(n)
            if bingo_board.win_check():
                return sum(bingo_board.unchecked_nums) * n
        i += 1

data = parseFile("./input.txt")
numbers = [int(i) for i in data[0].split(",")]

boards = parse_boards(data[2:])

print("q1", bingo(numbers, boards))

def bingo_last(numbers, boards):
    bingo_boards = [BingoBoard(board) for board in boards]
    i = 0
    last_board = None
    while i < len(numbers):
        n = numbers[i]
        for j in range(len(bingo_boards)-1, -1, -1):
            bingo_board = bingo_boards[j]
            bingo_board.update(n)
            if bingo_board.win_check():
                last_board = bingo_boards.pop(j)
                j += 1
            if len(bingo_boards) == 0:
                return sum(last_board.unchecked_nums) * n
        i += 1

print("q2", bingo_last(numbers, boards))


