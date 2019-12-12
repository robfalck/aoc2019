import networkx as nx
from part1 import build_tree


def part2(inp):
    tree = build_tree(inp, digraph=True)

    you_parent = list(tree.predecessors('YOU'))[0]
    san_parent = list(tree.predecessors('SAN'))[0]

    print(you_parent, san_parent)

    tree = build_tree(inp, digraph=False)

    shortest_path = nx.algorithms.shortest_path(tree, you_parent, san_parent)
    print(len(shortest_path) - 1)


if __name__ == '__main__':

    with open('input.txt') as f:
        inp = f.readlines()

    part2(inp)