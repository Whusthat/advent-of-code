from collections import Counter

with open('test.in') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    lines = [line.replace("->", "").split() for line in lines]

diagramm = []


def line_segement(string):
    z = string[0].split(",")
    u = string[1].split(",")
    x1 = z[0]
    y1 = z[1]
    x2 = u[0]
    y2 = u[1]

    if x1 == x2:
        if y1 < y2:
            diagramm.append([x2+str(x) for x in range(int(y1), int(y2)+1, 1)])
        else:
            diagramm.append([x2+str(x) for x in range(int(y2), int(y1)+1, 1)])
    if y1 == y2:
        if x1 < x2:
            diagramm.append([str(x)+y2 for x in range(int(x1), int(x2)+1, 1)])
        else:
            diagramm.append([str(x)+y2 for x in range(int(x2), int(x1)+1, 1)])


for line in lines:
    line_segement(line)


merged = []

for list in diagramm:
    for l in list:
        merged.append(l)


count = Counter(merged)

print(count)

count_amount = 0

for c in count:
    if count[c] > 1:
        count_amount = count_amount + 1

print(count_amount)
