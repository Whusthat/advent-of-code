from fishClass import Fish

# Handle Input
with open('input.in') as file:
    data = file.read().split(",")       # remove comma
    data = [int(x) for x in data]  # convert every char of str in int and wrap them in list


def count_fishes_a(intevals):

    fishes = [Fish(timer) for timer in intevals]        # create Fish objects with internal timer
    days = 80

    while days > 0:
        new_fishes = 0
        for fish in fishes:
            if fish.timer > 0:
                fish.timer -= 1
            else:
                new_fishes += 1
                fish.timer = 6
        days -= 1

        print(len(fishes))


count_fishes_a(data)






