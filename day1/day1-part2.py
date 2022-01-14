from readInput import read_input

#read input from file
input = read_input("input.txt")

totals = []

for index in range(len(input)):
    if (len(input) - index) > 3:
        sum = input[index] + input[index+1] + input[index+2]
        totals.append(sum)
       
j = 0
counter = 0

for i in totals:
    if i > j:
        counter += 1
    j = i   


print(counter)
