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
    if a > b:
        bitlist = [x for x in bitlist if not x[i] == "0"]
        return bitlist
    else:
        bitlist = [x for x in bitlist if not x[i] == "1"]
        return bitlist


j = loop(data, 0)
k = loop(j, 1)
n = loop(k, 2)
m = loop(n, 3)

print(a)
