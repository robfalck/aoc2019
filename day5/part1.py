from intcode_computer import IntCodeComputer

def part1():
    comp = IntCodeComputer()
    with open('input.txt') as f:
        instructions = f.read()
    output = comp.run_program(instructions, mem=10000)
    # print(output)

if __name__ == '__main__':
    part1()