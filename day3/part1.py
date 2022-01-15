from readInput import read_input
from chunkString import chunkString

binaryList = read_input("input.txt", 'false')

mergedList = ''.join(binaryList)

strippedList = list(chunkString(mergedList, 5))

gammaRate = ""

for column in strippedList:
    count = 0
    for bit in column[0]:
        bitHolder = int(bit)

        if bitHolder > 0:
            count += 1

    if count > (len(column[0]) - count):
        gammaRate += "1"
    else:
        gammaRate += "0"
