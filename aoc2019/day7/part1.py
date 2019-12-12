from itertools import permutations
from aoc2019.intcode_computer import IntCodeComputer
import multiprocessing as mp


def run_sequence(seq, program):
    input_signal = 0

    for phase_setting in seq:
        input_queue = mp.Queue()
        output_queue = mp.Queue()
        comp = IntCodeComputer(stdio=False)
        p = mp.Process(target=comp.run_program, args=(program,), kwargs={'mem': 10000,
                                                                         'input_queue': input_queue,
                                                                         'output_queue': output_queue})

        p.start()
        input_queue.put(phase_setting)
        input_queue.put(input_signal)
        input_signal = output_queue.get()
        p.join()
    return input_signal

def part1(inp):
    sequences = permutations(range(5))
    best_output = 0
    best_sequene = None
    for s in sequences:
        output_signal = run_sequence(s, inp)
        if output_signal > best_output:
            best_output = output_signal
            best_sequence = s
    print(best_sequence)
    print(best_output)


if __name__ == '__main__':

    # program = '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0'

    with open('input.txt') as f:
        program = f.read()

    part1(program)
