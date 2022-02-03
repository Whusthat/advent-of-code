# Input Handle
with open('input.in') as file:
    lines = file.readlines()
    lines = [x.replace("\n", "") for x in lines]
    output = []
    segments = []

    for line in lines:
        x, y = line.split(" | ")
        output.append(y)
        segments.append(x)


def count_output(dataset):

    unique_segments = (2, 4, 3, 7)
    simple_words = 0

    for out in dataset:
        segment = out.split()
        for seg in segment:
            if len(seg) in unique_segments:
                simple_words += 1

    return simple_words


print(f"Answer for Part1: ", count_output(output))