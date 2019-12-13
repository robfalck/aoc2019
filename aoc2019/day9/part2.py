from aoc2019.intcode_computer import IntCodeComputer
import multiprocessing as mp


if __name__ == '__main__':
    iq = mp.Queue()
    oq = mp.Queue()
    program = '1102,34915192,34915192,7,4,7,99,0'
    program = '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'
    with open('input.txt') as f:
        program = f.read()

    comp = IntCodeComputer(stdio=True, relative_base=0)
    # p = mp.Process(target=comp.run_program, args=(program,), kwargs={'mem': 10000,
    #                                                                  'input_queue': iq,
    #                                                                  'output_queues': [oq]})
    comp.run_program(program, mem=10000)

    # 3989758265: right answer!

    # p.start()
    # # iq.put(1)
    # p.join()
    #
    #
    # while True:
    #     try:
    #         print(oq.get(block=False))
    #     except:
    #         break

# incorrecrt: 203 - too low