import networkx as nx

def build_tree(inp, digraph=True):
    if digraph:
        tree = nx.DiGraph()
    else:
        tree = nx.Graph()
    tree.add_node('COM')
    for line in inp:
        center = line[:3]
        satellite = line[4:7]
        if center not in tree:
            tree.add_node(center)
        if satellite not in tree:
            tree.add_node(satellite)
        tree.add_edge(center, satellite)
    return tree

def part1(inp):
    tree = build_tree(inp)
    count = 0
    for node in tree:
        count += len(nx.algorithms.dag.ancestors(tree, node))

    print(count)

if __name__ == '__main__':

    with open('input.txt') as f:
        inp = f.readlines()

    part1(inp)