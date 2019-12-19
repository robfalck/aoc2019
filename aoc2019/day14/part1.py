import math
import networkx as nx
import numpy as np

import matplotlib.pyplot as plt

def parse_input(inp):
    G = nx.DiGraph()

    for line in inp:
        reagents, product = [s.strip() for s in line.split('=>')]

        # Parse the product apart
        pqty, product = product.split()

        if product not in G:
            G.add_node(product, quantity=0)

        # Parse the reagents
        for ingredient in reagents.split(','):
            rqty, reagent = ingredient.split()
            if reagent not in G:
                G.add_node(reagent, quantity=0)
            G.add_edge(reagent, product, ratio=(int(rqty), int(pqty)))

    return G

def make_product(product, quantity, tree):

    print('making', quantity, product)

    if product == 'ORE':
        tree.nodes[product]['quantity'] += quantity
    else:

        for reagent in tree.predecessors(product):
            reagent_per_reaction, product_per_reaction = tree.edges[reagent, product]['ratio']
            num_reactions = math.ceil(quantity / product_per_reaction)
            reagent_needed = num_reactions * reagent_per_reaction
            tree.nodes[reagent]['quantity'] += reagent_needed

    tree.remove_node(product)


def part1(inp):

    tree = parse_input(inp)

    # nx.draw(tree, with_labels=True, pos=nx.planar_layout(tree))

    next_product = 'FUEL'
    tree.nodes['FUEL']['quantity'] = 1

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

    print(tree.nodes['ORE']['quantity'])




if __name__ == '__main__':
    with open('input.txt') as f:
        inp = f.readlines()

    part1(inp)