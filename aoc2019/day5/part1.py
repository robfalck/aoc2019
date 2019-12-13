from aoc2019.intcode_computer import IntCodeComputer
import multiprocessing as mp


def part1():
    comp = IntCodeComputer(stdio=False)
    iq = mp.Queue()
    oq = mp.Queue()
    with open('input.txt') as f:
        instructions = f.read()
    iq.put(1)
    comp.run_program(instructions, mem=10000, input_queue=iq, output_queues=[oq])

    while True:
        try:
            print(oq.get(block=False))
        except:
            break

if __name__ == '__main__':
    part1()