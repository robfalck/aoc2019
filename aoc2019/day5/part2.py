from aoc2019.intcode_computer import IntCodeComputer
import multiprocessing as mp


def part2(program):
    """
    Didn't have to use multiprocessing for this, but it will come in handy later.
    """
    input_queue = mp.Queue()
    output_queue = mp.Queue()

    comp = IntCodeComputer(stdio=False)

    p = mp.Process(target=comp.run_program, args=(program,), kwargs={'mem': 10000,
                                                                     'input_queue': input_queue,
                                                                     'output_queues': [output_queue]})

    p.start()
    input_queue.put(5)
    output = output_queue.get()
    p.join()

    print(output)

if __name__ == '__main__':

    with open('input.txt') as f:
        program = f.read()
    part2(program)
