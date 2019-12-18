import numpy as np

def _built_state_mats(inp):

    vel = np.zeros((4, 3), dtype=int)
    pos = np.zeros((4, 3), dtype=int)

    inp = inp.replace('x=', '')
    inp = inp.replace('y=', '')
    inp = inp.replace('z=', '')
    inp = inp.replace('<', '')
    inp = inp.replace('>', '')
    inp = inp.replace(',', '')

    for i,line in enumerate(inp.split('\n')):
        pos[i, :] = [int(s) for s in line.split()]

    return pos, vel


def do_step(pos, vel):
    # Update velocity
    for i, irow in enumerate(pos):
        dv = np.zeros(3, dtype=int)
        for j, jrow in enumerate(pos):
            if j == i:
                continue
            gt = np.asarray(jrow > irow, dtype=int)
            lt = np.asarray(jrow < irow, dtype=int)
            dv += gt
            dv -= lt
        vel[i, :] += dv

    # Update position
    pos += vel

def part2(inp, steps=10):
    pos, vel = _built_state_mats(inp)
    pe = np.sum(np.abs(pos), axis=1)
    ke = np.sum(np.abs(vel), axis=1)

    for step in range(steps):

        do_step(pos, vel)

        # Update energy
        pe = np.sum(np.abs(pos), axis=1)
        ke = np.sum(np.abs(vel), axis=1)
        te = pe * ke

    print(pos)
    print(vel)
    print(pe)
    print(ke)
    print(te)
    print(np.sum(te))



if __name__ == '__main__':

    inp = '<x=-1, y=0, z=2>\n' \
          '<x=2, y=-10, z=-7>\n' \
          '<x=4, y=-8, z=8>\n' \
          '<x=3, y=5, z=-1>'

    # with open('input.txt') as f:
    #     inp = f.read()

    part2(inp, steps=2772)