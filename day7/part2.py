# Input Handle
import statistics

with open('input.in') as file:
    horizontalPositions = file.read().split(",")
    horizontalPositions = [int(x) for x in horizontalPositions]


def count_fuel(dataset):
    fuel = []
    positionToReach = int(statistics.median(dataset))

    fuel_tank = []

    for position in dataset:
        currentPosition = position
        distance = (max(currentPosition, positionToReach) - min(positionToReach, currentPosition))
        fuel_count = 0
        cost = 0
        for way in range(distance):
            cost += 1
            fuel_count += cost
        fuel_tank.append(fuel_count)
    fuel.append(sum(fuel_tank))

    return min(fuel)


print("Answer for Part2: ", count_fuel(horizontalPositions))

