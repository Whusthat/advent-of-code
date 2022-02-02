# Input Handle
with open('input.in') as file:
    horizontalPositions = file.read().split(",")
    horizontalPositions = [int(x) for x in horizontalPositions]


def count_fuel(dataset):

    fuel = []

    for pos in range(min(dataset), max(dataset) + 1):
        fuel.append(sum([abs(x - pos) for x in dataset]))

    return min(fuel)


print("Answer for Part1: ", count_fuel(horizontalPositions))
