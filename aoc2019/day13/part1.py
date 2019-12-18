import multiprocessing as mp
import numpy as np

from aoc2019.intcode_computer import IntCodeComputer


def part1(program):

    iq = mp.Queue()
    oq = mp.Queue()

    comp = IntCodeComputer(stdio=False, relative_base=0)
    p = mp.Process(target=comp.run_program, args=(program,), kwargs={'mem': 10000,
                                                                     'input_queue': iq,
                                                                     'output_queues': [oq]})
    # comp.run_program(program, mem=10000)

    p.start()
    p.join()

    # Get all outputs
    output = []
    while True:
        try:
            output.append(oq.get(block=False))
        except:
            break

    data = np.reshape(output, (len(output)//3, 3))

    # Now add the data to a dictionary, where each position gets a tile id
    screen = {}

    for i, row in enumerate(data):
        screen[row[0], row[1]] = row[2]

    print(len([k for (k, v) in screen.items() if v == 2]))


if __name__ == '__main__':
    with open('input.txt') as f:
        inp = f.read()

    part1(inp)

