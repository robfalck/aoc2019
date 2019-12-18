import numpy as np
from aoc2019.day12.part1 import _built_state_mats, do_step


def part2(inp):
    pos, vel = _built_state_mats(inp)

    pos0 = pos.copy()
    vel0 = vel.copy()

    # Find the velocity periods:
    count = 0

    vel_periods = np.zeros((4, 3), dtype=int)
    pos_periods = np.zeros((4, 3), dtype=int)

    # Find the velocity periods
    step = 0
    while True:
        do_step(pos, vel)

        for j in range(3):
            if np.all(vel[:, j] == vel0[:, j]) and np.all(pos[:, j] == pos0[:, j]) and pos_periods[0, j] == 0:
                print('vel period step', step + 1)
                print('pos period step', step + 1)
                vel_periods[:, j] = pos_periods[:, j] = step + 1
        if np.all(vel_periods > 0) and np.all(pos_periods > 0):
            break
        step += 1
    print(vel_periods)
    print(pos_periods)
    print(np.lcm.reduce(np.concatenate((vel_periods, pos_periods)).ravel()))




if __name__ == '__main__':

    inp = '<x=-1, y=0, z=2>\n' \
          '<x=2, y=-10, z=-7>\n' \
          '<x=4, y=-8, z=8>\n' \
          '<x=3, y=5, z=-1>'

    with open('input.txt') as f:
        inp = f.read()

    part2(inp)

    # too low: 155272637520
    # too high: 9011272417102194208
    #           484244804958744