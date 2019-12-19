import math
import networkx as nx
import numpy as np

import matplotlib.pyplot as plt

from aoc2019.day14.part1 import parse_input, make_product

def part2(inp):

    tree = parse_input(inp)

    # nx.draw(tree, with_labels=True, pos=nx.planar_layout(tree))

    low = 1000000
    high = 10000000

    while low != high:
        tree = parse_input(inp)
        next_product = 'FUEL'
        tree.nodes['FUEL']['quantity'] = fuel_made = (low + high) // 2

        while len(tree.nodes) > 1:

            # nx.draw(tree, with_labels=True)
            # plt.show()

            make_product(next_product, tree.nodes[next_product]['quantity'], tree)

            if len(tree.nodes) == 1:
                break

            paths = []
            for resource in tree.nodes:
                paths.extend(list(nx.all_simple_paths(tree, 'ORE', resource)))

            if not paths:
                break

            next_idx = np.argmax([len(p) for p in paths])
            next_product = paths[next_idx][-1]

        # nx.draw(tree, with_labels=True)
        # plt.show()

        ore_used = tree.nodes['ORE']['quantity']

        print(low, high, ore_used - 1_000_000_000_000)

        if ore_used > 1_000_000_000_000:
            high = fuel_made
        elif ore_used < 1_000_000_000_000:
            low = fuel_made
        else:
            break

        if (high - low) < 2:
            fuel_made = low
            break

    print(fuel_made)




if __name__ == '__main__':
    with open('input.txt') as f:
        inp = f.readlines()

    part2(inp)