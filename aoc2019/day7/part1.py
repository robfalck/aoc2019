from itertools import permutations
from aoc2019.day7.intcode_computer import IntCodeComputer
import pexpect


comp = IntCodeComputer()

def run_sequence(seq, program):
    input_signal = 0

    for phase_setting in seq:
        comp.run_program(program, phase_setting=phase_setting, input_signal=input_signal)
        input_signal = comp._output_value
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
