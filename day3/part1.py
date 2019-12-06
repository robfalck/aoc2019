import numpy as np



def populate_wire_set(instructions):
    """
    Create a set that contains every coordinate occupied by the wire.
    """
    loc = [0, 0]
    myset = set()
    myset.add(tuple(loc))
    for command in instructions:
        direction = command[0]
        distance = int(command[1:])
        delta = np.arange(distance, dtype=int)
        if direction == 'R':
            xs = loc[0] + delta
            ys = loc[1] * np.ones_like(xs, dtype=int)
        elif direction == 'L':
            xs = loc[0] - delta
            ys = loc[1] * np.ones_like(xs, dtype=int)
        elif direction == 'U':
            ys = loc[1] + delta
            xs = loc[0] * np.ones_like(ys, dtype=int)
        elif direction == 'D':
            ys = loc[1] - delta
            xs = loc[0] * np.ones_like(ys, dtype=int)

        loc = xs[-1], ys[-1]
        pairs = np.squeeze(np.dstack((xs, ys))).tolist()
        myset.update([tuple(p) for p in pairs])

    return  myset


if __name__ == '__main__':
    with open('input.txt') as f:
        wire1_instructions = f.readline().split(',')
        wire2_instructions = f.readline().split(',')

    # wire1_instructions = 'R8,U5,L5,D3'.split(',')
    # wire2_instructions = 'U7,R6,D4,L4'.split(',')
    #
    # print(wire1_instructions)
    # print(wire2_instructions)

    wire1 = populate_wire_set(wire1_instructions)
    wire2 = populate_wire_set(wire2_instructions)

    # import matplotlib.pyplot as plt
    #
    # for x, y in wire1:
    #     plt.plot(x, y, 'r.')
    #
    # for x, y in wire2:
    #     plt.plot(x, y, 'b.')
    #
    # plt.show()

    # print(len(wire1)
    intersections = wire1.intersection(wire2)

    min_dist = 1E8
    min_loc = (0, 0)

    for x, y in intersections:
        if x == 0 and y == 0:
            continue
        else:
            md = abs(x) + abs(y)
            if md < min_dist:
                min_dist = md
                min_loc = (x, y)

    print(min_dist)
    print(min_loc)
    #
    #


