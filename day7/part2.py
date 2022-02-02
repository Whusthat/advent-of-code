# Input Handle
with open('input.in') as file:
    horizontalPositions = file.read().split(",")
    horizontalPositions = [int(x) for x in horizontalPositions]

need = 168


def count_fuel(dataset):
    fuel = []
    positions = [y for y in range(min(dataset), max(dataset) + 1)]
    i = 0

    for data in dataset:

        current_pos = data
        destin_pos = positions[i]
        costs = 0
        counter = 0
        fuel_to_destin = []

        if current_pos > destin_pos:
            for x in range(destin_pos, current_pos):
                costs += 1
                counter += costs
                fuel_to_destin.append(counter)
        else:
            for x in range(current_pos, destin_pos):
                costs += 1
                counter += costs
                fuel_to_destin.append(counter)
        i += 1
        fuel.append(fuel_to_destin)

    return min(fuel)


print("Answer for Part2: ", count_fuel(horizontalPositions))
