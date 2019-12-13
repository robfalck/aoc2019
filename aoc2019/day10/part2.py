import numpy as np
from aoc2019.day10.part1 import part1

def input_to_matrix(inp):

    cols = inp.find('\n')
    split_inp = inp.split('\n')
    rows = len(split_inp)

    mat = np.zeros((rows, cols), dtype=int)

    for i, row in enumerate(split_inp):
        for j, col in enumerate(row):
            if split_inp[i][j] == '#':
                mat[j, i] = 1

    return mat

def sort_by_distance(rel_coords):
    sorted_rel_coords = sorted(rel_coords, key=lambda x: x[0]**2 + x[1]**2)
    return sorted_rel_coords

def part2(inp):

    laser_pos, num_viewable, all_coords = part1(inp)

    print('laser at', laser_pos)


    # all coords maps an angle (in microradians) to the bodies found at that angle
    # add int(2*pi * 1E6) to the negative ones and sort the angles, this will let us start at 0
    # then for each angle, zap the closest asteroid and proceed to the next angle
    angles = sorted(all_coords.keys())

    for angle in angles:
        if angle < 0:
            new_angle = angle + int(2*np.pi * 1E6)
            print(angle, new_angle, all_coords[angle])
            if new_angle not in all_coords:
                all_coords[new_angle] = all_coords[angle]
            else:
                all_coords[new_angle].extend(all_coords[angle])
            del all_coords[angle]
        else:
            pass
            print(angle, angle, all_coords[angle])

    # Sort those at each angle by distance
    angles = sorted(all_coords)
    for angle in angles:
        all_coords[angle] = sort_by_distance(all_coords[angle])

    # Zap em!
    zapped = []
    while all_coords:
        angles = sorted(all_coords)
        for angle in angles:
            print('zapping', all_coords[angle][0])
            zapped.append(all_coords[angle][0])
            del all_coords[angle][0]
            if len(all_coords[angle]) == 0:
                del all_coords[angle]

    print(f'zapped {len(zapped)} asteroids')
    print(zapped)
    print(f'200 zapped asteroid is at relative position', zapped[199])
    abs_pos_200 = np.asarray(zapped[199]) + laser_pos
    print(f'absolute position of 200 zapped asteroid is', abs_pos_200)
    print(f'puzzle answer is ', 100 * abs_pos_200[0] + abs_pos_200[1] )




    # mat = input_to_matrix(inp)
    # rows, cols = np.where(mat == 1)
    # asteroid_coords = list(zip(rows, cols))
    #
    # num_viewable_asteroids = {}
    #
    # for from_asteroid in asteroid_coords:
    #
    #     rel_coords = []
    #     for to_asteroid in asteroid_coords:
    #         # Don't try to observe the asteroid from itself
    #         if from_asteroid == to_asteroid:
    #             continue
    #         rel_coords.append(tuple((np.asarray(to_asteroid) - np.asarray(from_asteroid)).tolist()))
    #
    #     # Store the position of other asteroids as angles (microradians)
    #     unique_angles = set()
    #     for rel_coord in rel_coords:
    #         mr = int((np.arctan2(*rel_coord))*1.0E6)
    #         unique_angles.add(mr)
    #
    #     num_viewable_asteroids[from_asteroid] = len(unique_angles)
    #
    # best_coord = max(num_viewable_asteroids, key=num_viewable_asteroids.get)
    #
    # print('Best asteroid at:', best_coord)
    # print('Viewable asteroids:', num_viewable_asteroids[best_coord])

        # if 0 not in coord:
        #     reduced = Fraction(*coord)
        #     print(coord, reduced.numerator, reduced.denominator)
        # else:
        #     print(coord, coord[0], coord[1])


if __name__ == '__main__':
    with open('input.txt') as f:
        inp = f.read()
    #
    # inp = '.#....#####...#..\n' \
    #       '##...##.#####..##\n' \
    #       '##...#...#.#####.\n' \
    #       '..#.....#...###..\n' \
    #       '..#.#.....#....##' \
    #
    part2(inp)

