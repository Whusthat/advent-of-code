from readInput import read_input
from chunkString import chunkString


binaryList = read_input("input.txt", 'false')

mergedList = ''.join(binaryList)

strippedList = list(chunkString(mergedList, 5))

firstBit = ""

for column in strippedList:
    if column[0] == "1":
        firstBit += "1"
    else:
        firstBit += "0"

