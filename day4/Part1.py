with open("input.in") as fin:
    numbers = fin.readline().strip("\n")
    next(fin)
    boardData = [i for i in fin.read().split("\n")]
    boardData = list(filter(None, boardData))

holder = []

for board in boardData:
    holder.append([board[i:i + 3] for i in range(0, len(board), 3)])


def remove_whitespace(liste):
    j = []
    for liste in liste:
        h = []
        for str in liste:
            h.append(str.strip())
        j.append(h)
    return j


def bingo_round(number):
    for i, v in enumerate(finalBoards):
        print(v)


finalBoards = remove_whitespace(holder)

print(finalBoards[0][0])

bingo_round(12)





