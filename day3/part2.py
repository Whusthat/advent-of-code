with open("input.txt") as fin:
    data = [i for i in fin.read().strip().split("\n")]


def mostBit(str):
    ones = str.count("1")
    zero = str.count("0")
    if ones > zero:
        return 1
    else:
        return 0


def loop(bitlist, i):
    a = ""
    b = ""
    for bin in bitlist:
        if bin[i] == "1":
            a += bin[i]
        else:
            b += bin[i]
    if len(a) > len(b) or len(a) == len(b):
        bitlist = [x for x in bitlist if not x[i] == "0"]
        return bitlist
    else:
        bitlist = [x for x in bitlist if not x[i] == "1"]
        return bitlist


listHolder = loop(data, 0)

index = 1

while len(listHolder) > 1:
    listHolder = loop(listHolder, index)
    index += 1

oxygenGeneratorRating = str(listHolder[0])

print(int(oxygenGeneratorRating, 2))
