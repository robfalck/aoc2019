import numpy as np
from fractions import Fraction

def input_to_matrix(inp):

    cols = inp.find('\n')
    split_inp = inp.split('\n')
    rows = len(split_inp)

    mat = np.zeros((cols, rows), dtype=int)

    for i, row in enumerate(split_inp):
        for j, col in enumerate(row):
            if split_inp[i][j] == '#':
                mat[j, i] = 1

    return mat

def get_rel_pos(from_coord, mat):
    pass

def part1(inp):
    mat = input_to_matrix(inp)
    rows, cols = np.where(mat == 1)
    asteroid_coords = list(zip(rows, cols))

    num_viewable_asteroids = {}

    all_angles = {}

    for from_asteroid in asteroid_coords:

        rel_coords = []
        for to_asteroid in asteroid_coords:
            # Don't try to observe the asteroid from itself
            if from_asteroid == to_asteroid:
                continue
            rel_coords.append(tuple((np.asarray(to_asteroid) - np.asarray(from_asteroid)).tolist()))

        # Store the position of other asteroids as angles (microradians)
        unique_angles = set()
        all_angles[from_asteroid] = {}
        for rel_coord in rel_coords:
            angle_to_tgt = np.arctan2(rel_coord[1], rel_coord[0]) + np.pi / 2
            mr = int(angle_to_tgt*1E6)
            unique_angles.add(mr)
            if mr not in all_angles[from_asteroid]:
                all_angles[from_asteroid][mr] = [rel_coord]
            else:
                all_angles[from_asteroid][mr].append(rel_coord)

        num_viewable_asteroids[from_asteroid] = len(unique_angles)

    best_coord = max(num_viewable_asteroids, key=num_viewable_asteroids.get)

    print('Best asteroid at:', best_coord)
    print('Viewable asteroids:', num_viewable_asteroids[best_coord])

    return best_coord, num_viewable_asteroids, all_angles[best_coord]

        # if 0 not in coord:
        #     reduced = Fraction(*coord)
        #     print(coord, reduced.numerator, reduced.denominator)
        # else:
        #     print(coord, coord[0], coord[1])


if __name__ == '__main__':
    with open('input.txt') as f:
        inp = f.read()

    # inp = '.#..#\n' \
    #       '.....\n' \
    #       '#####\n' \
    #       '....#\n' \
    #       '...##'
    #
    # inp = '.#..##.###...#######\n' \
    #       '##.############..##.\n' \
    #       '.#.######.########.#\n' \
    #       '.###.#######.####.#.\n' \
    #       '#####.##.#.##.###.##\n' \
    #       '..#####..#.#########\n' \
    #       '####################\n' \
    #       '#.####....###.#.#.##\n' \
    #       '##.#################\n' \
    #       '#####.##.###..####..\n' \
    #       '..######..##.#######\n' \
    #       '####.##.####...##..#\n' \
    #       '.#####..#.######.###\n' \
    #       '##...#.##########...\n' \
    #       '#.##########.#######\n' \
    #       '.####.#.###.###.#.##\n' \
    #       '....##.##.###..#####\n' \
    #       '.#.#.###########.###\n' \
    #       '#.#.#.#####.####.###\n' \
    #       '###.##.####.##.#..##'



    part1(inp)

