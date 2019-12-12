from itertools import permutations
from aoc2019.intcode_computer import IntCodeComputer
import multiprocessing as mp

def part2(program):
    sequences = permutations(range(5, 10))

    best_output = 0
    best_sequence = None
    for seq in sequences:
        # Initialize our computers, each will run in its own process
        comp_a = IntCodeComputer(name='a', stdio=False)
        comp_b = IntCodeComputer(name='b', stdio=False)
        comp_c = IntCodeComputer(name='c', stdio=False)
        comp_d = IntCodeComputer(name='d', stdio=False)
        comp_e = IntCodeComputer(name='e', stdio=False)

        a_iq = mp.Queue()
        b_iq = mp.Queue()
        c_iq = mp.Queue()
        d_iq = mp.Queue()
        e_iq = mp.Queue()

        user_output_queue = mp.Queue()

        proc_a = mp.Process(target=comp_a.run_program, args=(program,),
                            kwargs={'mem': 10000, 'input_queue': a_iq,  'output_queues': [b_iq]})

        proc_b = mp.Process(target=comp_b.run_program, args=(program,),
                            kwargs={'mem': 10000, 'input_queue': b_iq,  'output_queues': [c_iq]})

        proc_c = mp.Process(target=comp_c.run_program, args=(program,),
                            kwargs={'mem': 10000, 'input_queue': c_iq,  'output_queues': [d_iq]})

        proc_d = mp.Process(target=comp_d.run_program, args=(program,),
                            kwargs={'mem': 10000, 'input_queue': d_iq,  'output_queues': [e_iq]})

        proc_e = mp.Process(target=comp_e.run_program, args=(program,),
                            kwargs={'mem': 10000, 'input_queue': e_iq,  'output_queues': [a_iq, user_output_queue]})

        # Put the phase setting on the queue for each thruster
        a_iq.put(seq[0])
        b_iq.put(seq[1])
        c_iq.put(seq[2])
        d_iq.put(seq[3])
        e_iq.put(seq[4])

        a_iq.put(0)

        # Start the processes
        proc_a.start()
        proc_b.start()
        proc_c.start()
        proc_d.start()
        proc_e.start()

        # Now run to completion
        proc_a.join()
        proc_b.join()
        proc_c.join()
        proc_d.join()
        proc_e.join()

        e_outputs = []
        while True:
            try:
                e_outputs.append(user_output_queue.get(block=False))
            except:
                break
        val = e_outputs[-1]

        if val > best_output:
            best_output = val
            best_sequence = seq

    print(best_output)
    print(best_sequence)

if __name__ == '__main__':

    # program = '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0'

    with open('input.txt') as f:
        program = f.read()

    part2(program)
