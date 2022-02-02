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
        holder = []
        for number in positions:
            fuel_to_destin = []
            current_pos = data
            destin_pos = number
            costs = 0
            counter = 0
            if current_pos > destin_pos:
                for x in range(destin_pos, current_pos):
                    costs += 1
                    counter += costs
                    fuel_to_destin.append(counter)
            elif current_pos == destin_pos:
                fuel_to_destin.append(1)
            else:
                for x in range(current_pos, destin_pos):
                    costs += 1
                    counter += costs
                    fuel_to_destin.append(counter)
            holder.append([sum(fuel_to_destin)])
        fuel.append(holder)
        i += 1


    print(fuel)


print("Answer for Part2: ", count_fuel(horizontalPositions))
