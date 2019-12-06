with open('input.txt') as wdf:
    line = wdf.readline()

tokens = [int(s) for s in line.split(',')]

tokens[1] = 12
tokens[2] = 2

# tokens = [1,9,10,3,2,3,11,0,99,30,40,50]


# def add(pos, tokens):
#     address_1 = tokens[pos + 1]
#     address_2 = tokens[pos + 2]
#     address_3 = tokens[pos + 3]
#     tokens[address_3] = tokens[address_1] + tokens[address_2]
#     return pos + 4, tokens
#
# def mul(pos, tokens):
#     address_1 = tokens[pos + 1]
#     address_2 = tokens[pos + 2]
#     address_3 = tokens[pos + 3]
#     tokens[address_3] = tokens[address_1] * tokens[address_2]
#     return pos + 4, tokens
#
#
#
# def process_instruction(pos, tokens):
#     halt = False
#     if tokens[pos] == 1:
#         pos, tokens = add(pos, tokens)
#     elif tokens[pos] == 2:
#         pos, tokens = mul(pos, tokens)
#     elif tokens[pos] == 99:
#         halt = True
#     else:
#         raise ValueError('unrecognized code', tokens[pos])
#     return pos, tokens, halt

from part1 import add, mul, process_instruction

def run_program(noun, verb):
    with open('input.txt') as wdf:
        line = wdf.readline()

    tokens = [int(s) for s in line.split(',')]

    tokens[1] = noun
    tokens[2] = verb
    pos = 0

    while True:
        pos, tokens, halt = process_instruction(pos, tokens)
        # print
        if halt:
            break

    return tokens[0]

if __name__ == '__main__':
    for i in range(99):
        for j in range(99):
            output = run_program(noun=i, verb=j)
            if output == 19690720:
                print(i, j, 100*i+j)
                exit(0)




# 10694