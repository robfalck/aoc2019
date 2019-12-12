from aoc2019.intcode_computer import IntCodeComputer

def part2(program):
    comp = IntCodeComputer()
    output = comp.run_program(program, mem=10000)
    # print(output)

if __name__ == '__main__':

    with open('input.txt') as f:
        program = f.read()
    # program = '3,9,8,9,10,9,4,9,99,-1,8'

    part2(program)