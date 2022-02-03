# Input Handle
with open('input.in') as file:
    horizontalPositions = file.read().split(",")
    horizontalPositions = [int(x) for x in horizontalPositions]


def count_fuel(dataset):

    # calc the increasing fuel costs
    def triangular_cost(steps):
        return steps * (steps + 1) // 2         # steps * (steps + 1) // 2 -> returns an int

    # create big number to check for lowest fuel
    minFuel = 2 << 100

    # loop over every possible position
    for position in range(min(dataset), max(dataset) + 1):
        fuel = 0
        # check every crab for the current target position
        for crab in dataset:
            fuel += triangular_cost(abs(position - crab))
        # only keep lowest fuel value, so you don not need a stack
        minFuel = min(fuel, minFuel)

    return minFuel


print("Answer for Part2: ", count_fuel(horizontalPositions))

