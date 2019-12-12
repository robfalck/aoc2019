from itertools import permutations
from aoc2019.day7.intcode_computer import IntCodeComputer
import subprocess


comp = IntCodeComputer()

def execute(program, phase_setting, power_level):
    proc = subprocess.Popen(['python', '../intcode_computer.py', program],
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)


    # print(proc.stdout.readline())
    proc.stdin.write(f'{phase_setting}\n'.encode())
    proc.stdin.flush()
    # print(proc.stdout.readline())
    proc.stdin.write(f'{power_level}\n'.encode())
    proc.stdin.flush()
    proc.stdin.flush()
    output = str(proc.stdout.readline()).strip()
    loc = output.rfind('t')
    print(output)
    print(loc)
    output = output[loc+1:]
    print(output)
    proc.stdin.close()
    proc.terminate()
    proc.wait(timeout=0.2)
    exit(0)


def run_sequence(seq, program):
    input_signal = 0

    for phase_setting in seq:
        execute(program, phase_setting, power_level=0)
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
