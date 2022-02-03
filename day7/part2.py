# Input Handle
with open('input.in') as file:
    horizontalPositions = file.read().split(",")
    horizontalPositions = [int(x) for x in horizontalPositions]

need = 168


def count_fuel(dataset):
    fuel = []
    finalFuel = []
    positionToReach = [x for x in range(max(dataset) + 1)]

    for reach in positionToReach:
        for i, position in enumerate(dataset):
            current_fuel = []
            count_current = 0
            for step in range(0, max(reach, position) - min(reach, position)):
                count_current += step + 1
                if step == (max(reach, position) - min(reach, position) - 1):
                    current_fuel.append(count_current)
            fuel.append(sum(current_fuel))
        finalFuel.append(sum(fuel))
        fuel.clear()

    return min(finalFuel)






print("Answer for Part2: ", count_fuel(horizontalPositions))
