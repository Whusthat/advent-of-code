# Input Handle
import statistics

with open('input.in') as file:
    horizontalPositions = file.read().split(",")
    horizontalPositions = [int(x) for x in horizontalPositions]


def count_fuel(dataset):

    # calc the increasing fuel costs
    def triangular_cost(steps):
        return steps * (steps + 1) // 2

    # create big number to check for lowest fuel
    minFuel = 2 << 100

    # loop over every possible position
    for position in range(min(dataset), max(dataset) + 1):
        fuel = 0
        for crab in dataset:
            crabPos = crab
            destinPos = position
            fuel += triangular_cost(abs(crabPos - destinPos))

            # only keep lowest fuel value, so you don not need a stack
        minFuel = min(fuel, minFuel)

    return minFuel


print("Answer for Part2: ", count_fuel(horizontalPositions))

