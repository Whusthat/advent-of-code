def remove_whitespace(liste):
    j = []
    for liste in liste:
        h = []
        for str in liste:
            h.append(str.strip())
        j.append(h)
    return j


with open("test.in") as fin:
    holder = []
    holderA = []
    numbers = fin.readline().strip("\n")
    numbers = numbers.split(",")
    next(fin)
    boardData = [i for i in fin.read().split("\n")]
    boardData = list(filter(None, boardData))
    for board in boardData:
        holder.append([board[i:i + 3] for i in range(0, len(board), 3)])
    final = remove_whitespace(holder)
    boards = ([final[i:i + 5] for i in range(0, len(final), 5)])


class Board:
    row = 0
    column = 0

    def __init__(self, list):
        self.board = list

    def round(self, number):
        for i, b in enumerate(self.board):
            for z, c in enumerate(b):
                if c == number:
                    b[z] = "hit"
        self.winner()

    def winner(self):
        for i, b in enumerate(self.board):
            for z, c in enumerate(b):
                if b[z] == "hit":
                    self.row = self.row + 1
                if z > 4:
                    self.row = 0
                if self.row == 5:
                    print(self)
                    return True


objs = [Board(i) for i in boards]


def play(er):
    for num in er:
        for obj in objs:
            if obj.round(num):
                return obj


play(numbers)