from readInput import read_input
from chunkString import chunkString

binaryList = read_input("input.txt", 'false')

j = [0, 0]
k = [0, 0]
n = [0, 0]
m = [0, 0]
o = [0, 0]

mergedList = ''.join(binaryList)

strippedList = list(chunkString(mergedList, 5))

for item in strippedList:
    for i, v in enumerate(item):

        if (i == 0) and (v == '1'):
            j[0] += 1
        else:
            j[1] += 1

        if (i == 1) and (v == '1'):
            k[0] += 1
        else:
            k[1] += 1

        if (i == 2) and (v == '1'):
            n[0] += 1
        else:
            n[1] += 1

        if (i == 3) and (v == '1'):
            m[0] += 1
        else:
            m[1] += 1

        if (i == 4) and (v == '1'):
            o[0] += 1
        else:
            o[1] += 1


def getBin(x):
    if x[0] > x[1]:
        return 1
    else:
        return 0


firstBit = getBin(j)
secondBit = getBin(k)
thirdBit = getBin(n)
fourthBit = getBin(m)
fithBit = getBin(o)

print(fithBit)