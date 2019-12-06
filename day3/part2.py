import numpy as np



def populate_wire_set(instructions):
    """
    Create a set that contains every coordinate occupied by the wire.
    In part 2 the set is replaced with a dict where the location (key) maps to the steps to get there (value)
    """
    # print('populating wire ', instructions)
    loc = [0, 0]
    cumdist = 0
    mydict = {}
    for command in instructions:
        direction = command[0]
        distance = int(command[1:])
        delta = np.arange(distance+1, dtype=int)
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

        for i, p in enumerate(pairs):
            tp = tuple(p)
            if tp not in mydict:
                mydict[tp] = cumdist + i

        # mydict.update({tuple(p): cumdist+i for (i, p) in enumerate(pairs)})
        cumdist += distance

    # print('total wire length', cumdist)
    # print('wire dict')
    # for k in mydict:
        # print('    ', k, mydict[k])

    return  mydict


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
    intersections = set(wire1.keys()).intersection(set(wire2.keys()))

    min_loc = (0, 0)
    min_steps = 10E8

    for x, y in intersections:
        # print('intersection', x, y)
        # print('wire1:', wire1[(x, y)])
        # print('wire2:', wire2[(x, y)])
        if x == 0 and y == 0:
            continue
        else:
            ms = wire1[(x, y)] + wire2[(x, y)]
            if ms < min_steps:
                min_steps = ms
                min_loc = (x, y)

    print(min_loc)
    print(wire1[min_loc])
    print(wire2[min_loc])
    print(min_steps)
    #
    #

    # 20254 too low

