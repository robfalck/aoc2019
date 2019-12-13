import numpy as np
from aoc2019.intcode_computer import IntCodeComputer
import multiprocessing as mp


class Robot(object):

    def __init__(self):
        self.loc = (0, 0)
        self.heading = (0, 1)

    def turn_left_and_move(self):
        if self.heading == (0, 1):
            self.heading = (-1, 0)
        elif self.heading == (-1, 0):
            self.heading = (0, -1)
        elif self.heading == (0, -1):
            self.heading = (1, 0)
        elif self.heading == (1, 0):
            self.heading = (0, 1)
        self.loc = tuple(np.asarray(self.loc) + np.asarray(self.heading))

    def turn_right_and_move(self):
        if self.heading == (0, 1):
            self.heading = (1, 0)
        elif self.heading == (1, 0):
            self.heading = (0, -1)
        elif self.heading == (0, -1):
            self.heading = (-1, 0)
        elif self.heading == (-1, 0):
            self.heading = (0, 1)
        self.loc = tuple(np.asarray(self.loc) + np.asarray(self.heading))


if __name__ == '__main__':
    iq = mp.Queue()
    oq = mp.Queue()
    with open('input.txt') as f:
        program = f.read()

    surface = {}
    painter = Robot()

    comp = IntCodeComputer(stdio=False, relative_base=0)
    p = mp.Process(target=comp.run_program, args=(program,), kwargs={'mem': 10000,
                                                                     'input_queue': iq,
                                                                     'output_queues': [oq]})

    iq.put(0)
    p.start()

    while p.is_alive():
        try:
            paint_color = oq.get(timeout=1)
            next_move = oq.get(timeout=1)
        except:
            break

        surface[painter.loc] = paint_color
        if next_move == 0:
            painter.turn_left_and_move()
        elif next_move == 1:
            painter.turn_right_and_move()
        # print(paint_color, next_move)
        if painter.loc in surface:
            iq.put(surface[painter.loc])
        else:
            iq.put(0)

    print(len(surface))
