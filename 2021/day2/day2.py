f = open('input.txt')
inp = [i for i in f.read().splitlines()]

test = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]


def sol_1(i):

    positions = {"horizontal": 0, "depth": 0}
    delta = {"down": 1, "up": -1, "forward": 1}
    axis = {"forward": "horizontal", "down": "depth", "up": "depth"}

    for line in i:
        line_list = line.split()
        direction, amount = line_list[0], int(line_list[1])

        positions[axis[direction]] = positions[axis[direction]] + amount * delta[direction]

    return positions["horizontal"] * positions["depth"]




def sol_2(i):

    positions = {"horizontal": 0, "aim": 0, "depth": 0}
    delta = {"down": 1, "up": -1, }

    for line in i:
        line_list = line.split()
        direction, amount = line_list[0], int(line_list[1])

        if direction == "forward":
            positions["horizontal"] = positions["horizontal"] + amount
            positions["depth"] = positions["depth"] + (positions["aim"] * amount)
        else:
            positions["aim"] = positions["aim"] + amount * delta[direction]

    return positions["horizontal"] * positions["depth"]

print(sol_2(inp))

